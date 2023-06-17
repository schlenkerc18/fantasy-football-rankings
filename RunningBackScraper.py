import pandas as pd
import re
import requests
from bs4 import BeautifulSoup


def scrape_data(year, columns):
    url = requests.get(f'https://www.fantasypros.com/nfl/stats/rb.php?year={year}')
    src = url.content
    soup = BeautifulSoup(src, 'html.parser')
    
    final_df = pd.DataFrame(columns = columns)

    # pull in player rows
    players = soup.find_all('tr', attrs = {'class': re.compile('mpb-player-')})
    
    for player in players:
            
        # get the stats for each player
        stats = [stat.get_text() for stat in player.find_all('td')]
        
        # create a dataframe for the single player's stats
        temp_df = pd.DataFrame(stats).transpose()
        temp_df['Year'] = year
        temp_df.columns = columns
        
        # Join the single player's stats with the overall dataset
        final_df = pd.concat([final_df, temp_df], ignore_index = True)

    return final_df



if __name__ == '__main__':
    # create column names
    columns = ['RANK', 'PLAYER', 'ATT', 'YDS', 'Y/A', 'LG', '20+', 'TD', 'REC',
               'TGT', 'YDS', 'Y/R', 'TD', 'FL', 'G', 'FPTS', 'FPTS/G', 'OWN', 'Year']

    # list of years to scrape
    years_to_scrape = ['2018', '2019', '2020', '2021', '2022', '2023']

    # create dataframe to append to
    df = pd.DataFrame(columns=columns)

    for year in years_to_scrape:
        curr_df = scrape_data(year, columns)
        df = pd.concat([df, curr_df], ignore_index=True)

    df.to_csv("./StatFiles/rb_stats.csv", index=False)
