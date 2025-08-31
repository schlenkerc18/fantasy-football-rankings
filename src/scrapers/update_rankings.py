#!/usr/bin/env python3
"""
Script to update fantasy football rankings with 2024 actual finishes and calculate prediction accuracy.
Matches players between stat files and ranking files, then fills in missing columns.
"""

import pandas as pd
import os
import re
from pathlib import Path

class RankingsUpdater:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.stats_dir = self.base_dir / "StatFiles"
        self.rankings_dir = self.base_dir / "NFLYearlyTiers" / "2024"
        
        # Position mappings
        self.position_files = {
            'qb': {'stats': 'qb_stats.csv', 'rankings': 'qb_ratings_2024.xlsx'},
            'rb': {'stats': 'rb_stats.csv', 'rankings': 'rb_ratings_2024.xlsx'},
            'wr': {'stats': 'wr_stats.csv', 'rankings': 'wr_ratings_2024.xlsx'},
            'te': {'stats': 'te_stats.csv', 'rankings': 'te_ratings_2024.xlsx'}
        }
    
    def clean_player_name(self, name):
        """Clean player name for matching by removing team info and extra characters."""
        if pd.isna(name):
            return ""
        
        # Remove team abbreviations in parentheses (e.g., "(KC)", "(FA)")
        name = re.sub(r'\s*\([^)]*\)', '', str(name))
        
        # Remove common suffixes like Jr., Sr., II, III, IV
        name = re.sub(r'\s+(Jr\.?|Sr\.?|II|III|IV)$', '', name, flags=re.IGNORECASE)
        
        # Handle common name variations
        name = name.replace('Jonathon', 'Jonathan')  # Standardize Jonathan/Jonathon
        
        # Clean up extra whitespace
        name = ' '.join(name.split())
        
        return name.strip()
    
    def load_stats_data(self, position):
        """Load and filter stats data for 2024."""
        stats_file = self.stats_dir / self.position_files[position]['stats']
        
        if not stats_file.exists():
            print(f"Stats file not found: {stats_file}")
            return None
        
        # Load stats data
        stats_df = pd.read_csv(stats_file)
        
        # Filter for 2024 data
        stats_2024 = stats_df[stats_df['Year'] == 2024].copy()
        
        if stats_2024.empty:
            print(f"No 2024 data found in {stats_file}")
            return None
        
        # Clean player names
        stats_2024['PLAYER_CLEAN'] = stats_2024['PLAYER'].apply(self.clean_player_name)
        
        # Sort by RANK to get actual 2024 finish positions
        stats_2024 = stats_2024.sort_values('RANK').reset_index(drop=True)
        
        return stats_2024
    
    def load_rankings_data(self, position):
        """Load rankings data from Excel file."""
        rankings_file = self.rankings_dir / self.position_files[position]['rankings']
        
        if not rankings_file.exists():
            print(f"Rankings file not found: {rankings_file}")
            return None
        
        try:
            # Try to read Excel file
            rankings_df = pd.read_excel(rankings_file)
            
            # Clean player names
            if 'Player' in rankings_df.columns:
                rankings_df['PLAYER_CLEAN'] = rankings_df['Player'].apply(self.clean_player_name)
            else:
                print(f"No 'Player' column found in {rankings_file}")
                print(f"Available columns: {list(rankings_df.columns)}")
                return None
            
            return rankings_df
            
        except Exception as e:
            print(f"Error reading Excel file {rankings_file}: {e}")
            return None
    
    def match_players(self, stats_df, rankings_df):
        """Match players between stats and rankings dataframes."""
        matches = []
        unmatched_rankings = []
        
        for idx, ranking_row in rankings_df.iterrows():
            ranking_name = ranking_row['PLAYER_CLEAN']
            
            # Try exact match first
            exact_match = stats_df[stats_df['PLAYER_CLEAN'] == ranking_name]
            
            if not exact_match.empty:
                match_row = exact_match.iloc[0]
                matches.append({
                    'rankings_idx': idx,
                    'stats_idx': match_row.name,
                    'player_name': ranking_row['Player'],
                    'actual_finish': match_row['RANK'],
                    'match_type': 'exact'
                })
            else:
                # Try case-insensitive exact match
                case_insensitive_match = stats_df[stats_df['PLAYER_CLEAN'].str.lower() == ranking_name.lower()]
                
                if not case_insensitive_match.empty:
                    match_row = case_insensitive_match.iloc[0]
                    matches.append({
                        'rankings_idx': idx,
                        'stats_idx': match_row.name,
                        'player_name': ranking_row['Player'],
                        'actual_finish': match_row['RANK'],
                        'match_type': 'case_insensitive'
                    })
                else:
                    # Try partial matching with first and last name
                    name_parts = ranking_name.split()
                    if len(name_parts) >= 2:
                        first_name = name_parts[0]
                        last_name = name_parts[-1]
                        
                        # Look for players with matching first and last name
                        partial_matches = stats_df[
                            stats_df['PLAYER_CLEAN'].str.contains(first_name, case=False, na=False) &
                            stats_df['PLAYER_CLEAN'].str.contains(last_name, case=False, na=False)
                        ]
                        
                        if len(partial_matches) == 1:
                            match_row = partial_matches.iloc[0]
                            matches.append({
                                'rankings_idx': idx,
                                'stats_idx': match_row.name,
                                'player_name': ranking_row['Player'],
                                'actual_finish': match_row['RANK'],
                                'match_type': 'partial'
                            })
                        else:
                            unmatched_rankings.append({
                                'rankings_idx': idx,
                                'player_name': ranking_row['Player'],
                                'clean_name': ranking_name,
                                'partial_matches': len(partial_matches)
                            })
                    else:
                        unmatched_rankings.append({
                            'rankings_idx': idx,
                            'player_name': ranking_row['Player'],
                            'clean_name': ranking_name,
                            'partial_matches': 0
                        })
        
        return matches, unmatched_rankings
    
    def update_rankings_file(self, position):
        """Update rankings file with 2024 finish and prediction accuracy."""
        print(f"\nProcessing {position.upper()} position...")
        
        # Load data
        stats_df = self.load_stats_data(position)
        rankings_df = self.load_rankings_data(position)
        
        if stats_df is None or rankings_df is None:
            print(f"Skipping {position} due to missing data")
            return False
        
        # Match players
        matches, unmatched = self.match_players(stats_df, rankings_df)
        
        print(f"Found {len(matches)} matches, {len(unmatched)} unmatched players")
        
        # Initialize new columns if they don't exist
        if '2024 Finish' not in rankings_df.columns:
            rankings_df['2024 Finish'] = None
        if 'Pred vs Actual Finish' not in rankings_df.columns:
            rankings_df['Pred vs Actual Finish'] = None
        
        # Update matched players
        for match in matches:
            rankings_idx = match['rankings_idx']
            actual_finish = match['actual_finish']
            
            # Update 2024 Finish
            rankings_df.loc[rankings_idx, '2024 Finish'] = actual_finish
            
            # Calculate prediction accuracy (absolute difference)
            if 'PreRank' in rankings_df.columns:
                pre_rank = rankings_df.loc[rankings_idx, 'PreRank']
                if pd.notna(pre_rank):
                    pred_vs_actual = abs(int(pre_rank) - int(actual_finish))
                    rankings_df.loc[rankings_idx, 'Pred vs Actual Finish'] = pred_vs_actual
        
        # Remove the PLAYER_CLEAN column before saving
        if 'PLAYER_CLEAN' in rankings_df.columns:
            rankings_df = rankings_df.drop('PLAYER_CLEAN', axis=1)
        
        # Save updated rankings
        output_file = self.rankings_dir / f"{position}_ratings_2024_updated.xlsx"
        rankings_df.to_excel(output_file, index=False)
        print(f"Updated rankings saved to: {output_file}")
        
        # Print unmatched players for review
        if unmatched:
            print(f"\nUnmatched players in {position} rankings:")
            for player in unmatched[:10]:  # Show first 10
                print(f"  - {player['player_name']} (cleaned: {player['clean_name']})")
            if len(unmatched) > 10:
                print(f"  ... and {len(unmatched) - 10} more")
        
        return True
    
    def run_all_positions(self):
        """Process all positions."""
        print("Starting Fantasy Football Rankings Update...")
        print("=" * 50)
        
        success_count = 0
        for position in self.position_files.keys():
            if self.update_rankings_file(position):
                success_count += 1
        
        print(f"\n" + "=" * 50)
        print(f"Completed! Successfully processed {success_count}/{len(self.position_files)} positions")
        
        if success_count > 0:
            print("\nUpdated files saved with '_updated' suffix in the NFLYearlyTiers/2024/ directory")

def main():
    # Set base directory
    base_dir = Path(__file__).parent
    
    # Create updater and run
    updater = RankingsUpdater(base_dir)
    updater.run_all_positions()

if __name__ == "__main__":
    main()
