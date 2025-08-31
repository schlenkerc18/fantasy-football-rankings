import streamlit as st
import pandas as pd
import os
import json
from pathlib import Path
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI()

# Set page config
st.set_page_config(
    page_title="Fantasy Football Draft Board 2025",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define paths
BASE_DIR = Path(__file__).parent
RATINGS_DIR = BASE_DIR / "NFLYearlyTiers" / "2025"
STATS_DIR = BASE_DIR / "scrapers" / "StatFiles"
TEMP_FILE = BASE_DIR / "draft_board_state.json"

def load_ratings_files():
    """Load all 2025 rating files and combine them into a single DataFrame"""
    all_players = []
    
    position_files = {
        'QB': RATINGS_DIR / 'qb_ratings_2025.xlsx',
        'RB': RATINGS_DIR / 'rb_ratings_2025.xlsx',
        'WR': RATINGS_DIR / 'wr_ratings_2025.xlsx',
        'TE': RATINGS_DIR / 'te_ratings_2025.xlsx'
    }
    
    for position, file_path in position_files.items():     
        if file_path.exists():
            try:
                df = pd.read_excel(file_path)           
                # Add position column if not present
                if 'Position' not in df.columns:
                    df['Position'] = position
                # Ensure we have player name and rank columns
                if 'Player' in df.columns:
                    # Keep relevant columns
                    cols_to_keep = ['Player', 'Position']
                    if 'PreRank' in df.columns:
                        cols_to_keep.append('PreRank')
                    if 'Rating' in df.columns:
                        cols_to_keep.append('Rating')
                    if 'Tier' in df.columns:
                        cols_to_keep.append('Tier')
                    if 'ECR' in df.columns:
                        cols_to_keep.append('ECR')
                    
                    df_subset = df[cols_to_keep].copy()
                    # Add overall rank across all positions
                    df_subset['Overall_Rank'] = df_subset.get('PreRank', range(1, len(df_subset) + 1))
                    all_players.append(df_subset)
                else:
                    st.warning(f"No 'Player' column found in {position} file")
            except Exception as e:
                st.error(f"Error loading {position} file: {e}")
    
    if all_players:
        combined_df = pd.concat(all_players, ignore_index=True)
        # Sort by Rating if available, otherwise by PreRank
        if 'Rating' in combined_df.columns:
            combined_df = combined_df.sort_values('Rating', ascending=False).reset_index(drop=True)
        elif 'PreRank' in combined_df.columns:
            combined_df = combined_df.sort_values('PreRank', ascending=False).reset_index(drop=True)
        combined_df['Draft_Order'] = range(1, len(combined_df) + 1)
        return combined_df
    else:
        return pd.DataFrame()

def load_stats_files():
    """Load all historical stats CSV files"""
    stats_data = {}
    
    stats_files = {
        'QB': STATS_DIR / 'qb_stats.csv',
        'RB': STATS_DIR / 'rb_stats.csv',
        'WR': STATS_DIR / 'wr_stats.csv',
        'TE': STATS_DIR / 'te_stats.csv'
    }
    
    for position, file_path in stats_files.items():
        if file_path.exists():
            try:
                df = pd.read_csv(file_path)
                df['Position'] = position
                stats_data[position] = df
            except Exception as e:
                st.error(f"Error loading {position} stats: {e}")
    
    return stats_data

def save_state(drafted_players):
    """Save the list of drafted players to a temp file"""
    with open(TEMP_FILE, 'w') as f:
        json.dump(drafted_players, f)

def load_state():
    """Load the list of drafted players from temp file"""
    if TEMP_FILE.exists():
        try:
            with open(TEMP_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def reset_draft():
    """Reset the draft by removing the temp file"""
    if TEMP_FILE.exists():
        os.remove(TEMP_FILE)
    st.session_state.drafted_players = []
    st.rerun()

def main():
    st.title("🏈 Fantasy Football Draft Board 2025")
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Draft Board", "Player Stats", "AI Chat"])
    
    with tab1:
        draft_board_tab()
    
    with tab2:
        player_stats_tab()
    
    with tab3:
        ai_chat_tab()

def draft_board_tab():
    # Left align with reduced width (40% of total width)
    col1, col2 = st.columns([4, 6])
    with col1:
        # Initialize session state
        if 'drafted_players' not in st.session_state:
            st.session_state.drafted_players = load_state()
        
        if 'all_players_df' not in st.session_state:
            st.session_state.all_players_df = load_ratings_files()
        
        # Main content area
        if st.session_state.all_players_df.empty:
            st.error("No player data found. Please check that rating files exist in the 2025 folder.")
            return
        
        # Get filter values from session state (set by sidebar)
        position_filter = st.session_state.get('position_filter', ['QB', 'RB', 'WR', 'TE'])
        search_term = st.session_state.get('search_term', "")
        
        # Filter out drafted players
        available_players = st.session_state.all_players_df[
            ~st.session_state.all_players_df['Player'].isin(st.session_state.drafted_players)
        ].copy()
        
        # Apply position filter
        if position_filter:
            available_players = available_players[
                available_players['Position'].isin(position_filter)
            ]
        
        # Apply search filter
        if search_term:
            available_players = available_players[
                available_players['Player'].str.contains(search_term, case=False, na=False)
            ]
        
        # Display available players
        st.header("Available Players")
        
        if available_players.empty:
            st.info("No players available with current filters.")
        else:
            # Create columns for the draft board
            for idx, row in available_players.iterrows():
                dcol1, dcol2, dcol3, dcol4, dcol5, dcol6 = st.columns([1, 3, 1, 1, 1, 1])
                
                with dcol1:
                    st.write(f"#{row.get('Draft_Order', '')}")
                
                with dcol2:
                    st.write(f"**{row['Player']}**")
                
                with dcol3:
                    # Display position with color coding
                    position_colors = {
                        'QB': '🔴',
                        'RB': '🔵',
                        'WR': '🟢',
                        'TE': '🟡'
                    }
                    st.write(f"{position_colors.get(row['Position'], '⚪')} {row['Position']}")
                
                with dcol4:
                    if 'Tier' in row:
                        st.write(f"Tier {row['Tier']}")
                
                with dcol5:
                    if 'ECR' in row and pd.notna(row['ECR']):
                        st.write(f"ECR: {row['ECR']:.1f}")
                
                with dcol6:
                    # Draft button for each player
                    if st.button("Draft", key=f"draft_{row['Player']}", type="secondary"):
                        st.session_state.drafted_players.append(row['Player'])
                        save_state(st.session_state.drafted_players)
                        st.rerun()
        
        # Show recently drafted players
        if st.session_state.drafted_players:
            st.header("Recently Drafted")
            recent_drafted = st.session_state.drafted_players[-5:][::-1]  # Show last 5, most recent first
            for player in recent_drafted:
                st.write(f"✓ {player}")
    
    # Sidebar controls (keep outside column structure)
    with st.sidebar:
        st.header("Draft Controls")
        
        # Reset button
        if st.button("🔄 Reset Draft", type="primary", use_container_width=True):
            reset_draft()
        
        # Filter by position
        st.session_state.position_filter = st.multiselect(
            "Filter by Position",
            options=['QB', 'RB', 'WR', 'TE'],
            default=['QB', 'RB', 'WR', 'TE']
        )
        
        # Search player
        st.session_state.search_term = st.text_input("🔍 Search Player", "")
        
        # Draft statistics
        st.header("Draft Statistics")
        total_players = len(st.session_state.all_players_df)
        drafted_count = len(st.session_state.drafted_players)
        available_count = total_players - drafted_count
        
        scol1, scol2 = st.columns(2)
        with scol1:
            st.metric("Total Players", total_players)
            st.metric("Drafted", drafted_count)
        with scol2:
            st.metric("Available", available_count)
            progress = drafted_count / total_players if total_players > 0 else 0
            st.progress(progress)

def player_stats_tab():
    st.header("📊 Historical Player Stats (2018-2024)")
    
    # Load stats data
    if 'stats_data' not in st.session_state:
        st.session_state.stats_data = load_stats_files()
    
    if not st.session_state.stats_data:
        st.error("No stats data found. Please check that CSV files exist in StatFiles folder.")
        return
    
    # Sidebar filters for stats
    with st.sidebar:
        st.header("Stats Filters")
        
        # Position filter
        selected_position = st.selectbox(
            "Select Position",
            options=['QB', 'RB', 'WR', 'TE'],
            index=0
        )
        
        # Year filter
        if selected_position in st.session_state.stats_data:
            available_years = sorted(st.session_state.stats_data[selected_position]['Year'].unique(), reverse=True)
            selected_years = st.multiselect(
                "Select Years",
                options=available_years,
                default=available_years  # Default to all years
            )
            
            # Player search
            stats_search = st.text_input("🔍 Search Player (Stats)", "")
            
            # Minimum games filter
            min_games = st.slider("Minimum Games Played", 1, 17, 8)
    
    # Display stats
    if selected_position in st.session_state.stats_data:
        df = st.session_state.stats_data[selected_position].copy()
        
        # Apply filters
        if selected_years:
            df = df[df['Year'].isin(selected_years)]
        
        if stats_search:
            df = df[df['PLAYER'].str.contains(stats_search, case=False, na=False)]
        
        df = df[df['G'] >= min_games]
        
        if df.empty:
            st.info("No players match the current filters.")
        else:
            # Sort by Year descending first, then by fantasy points per game
            df = df.sort_values(['Year', 'FPTS/G'], ascending=[False, False]).reset_index(drop=True)
            
            # Display summary stats
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Players", len(df))
            with col2:
                st.metric("Avg FPTS/G", f"{df['FPTS/G'].mean():.1f}")
            with col3:
                st.metric("Top FPTS/G", f"{df['FPTS/G'].max():.1f}")
            with col4:
                st.metric("Years Shown", len(selected_years))
            
            # Display the data table
            st.subheader(f"{selected_position} Stats")
            
            # Format numeric columns for better display
            display_df = df.copy()
            numeric_cols = display_df.select_dtypes(include=['float64', 'int64']).columns
            for col in numeric_cols:
                if col in ['FPTS', 'FPTS/G']:
                    display_df[col] = display_df[col].round(1)
                elif col in ['PCT', 'Y/A', 'Y/R']:
                    display_df[col] = display_df[col].round(1)
            
            # Show top 50 players
            st.dataframe(
                display_df.head(50),
                use_container_width=True,
                hide_index=True
            )
            
            # Show player comparison if multiple years selected
            if len(selected_years) > 1 and stats_search:
                st.subheader("Year-over-Year Comparison")
                player_data = df[df['PLAYER'].str.contains(stats_search, case=False, na=False)]
                if not player_data.empty:
                    # Create a simple line chart for FPTS/G over years
                    chart_data = player_data.pivot_table(
                        index='Year', 
                        columns='PLAYER', 
                        values='FPTS/G', 
                        aggfunc='first'
                    )
                    st.line_chart(chart_data)

def get_ai_response(user_message):
    """Get response from OpenAI API"""
    try:
        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {"role": "system", "content": "You are a helpful fantasy football assistant. Answer questions about fantasy football, player analysis, draft strategy, and general football knowledge. Be concise and informative."},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"API error: {e}"

def ai_chat_tab():
    # Left align with reduced width (40% of total width)
    col1, col2 = st.columns([4, 6])
    with col1:
        st.header("🤖 AI Fantasy Football Assistant")
        
        # Initialize chat history in session state
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # Chat input
        user_input = st.text_area(
            "Ask me anything about fantasy football:",
            placeholder="e.g., Should I draft a RB or WR in the first round? What do you think about Patrick Mahomes this season?",
            height=100
        )
        
        # Send button
        ccol1, ccol2 = st.columns([1, 4])
        with ccol1:
            if st.button("Send", type="primary", use_container_width=True):
                if user_input.strip():
                    # Add user message to history
                    st.session_state.chat_history.append({"role": "user", "content": user_input})
                    
                    # Get AI response
                    with st.spinner("Getting AI response..."):
                        ai_response = get_ai_response(user_input)
                    
                    # Add AI response to history
                    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                    
                    # Clear input and rerun
                    st.rerun()
        
        with ccol2:
            if st.button("Clear Chat", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()
        
        # Display chat history
        if st.session_state.chat_history:
            st.subheader("Conversation")
            
            for i, message in enumerate(st.session_state.chat_history):
                if message["role"] == "user":
                    st.markdown(f"**You:** {message['content']}")
                else:
                    st.markdown(f"**AI Assistant:** {message['content']}")
                
                # Add some spacing between messages
                if i < len(st.session_state.chat_history) - 1:
                    st.markdown("---")
        else:
            st.info("Start a conversation by asking a question about fantasy football!")

if __name__ == "__main__":
    main()
