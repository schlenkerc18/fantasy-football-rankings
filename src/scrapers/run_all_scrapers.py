import concurrent.futures
import time
from datetime import datetime
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

# Import the scraper functions from each file
from QuarterBackScraper import scrape_data as qb_scrape
from RunningBackScraper import scrape_data as rb_scrape
from TightEndScraper import scrape_data as te_scrape
from WideReceiverScraper import scrape_data as wr_scrape


def run_qb_scraper():
    """Run the quarterback scraper and save to CSV"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting QB scraper...")
    
    columns = ['RANK', 'PLAYER', 'CMP', 'ATT', 'PCT', 'YDS', 'Y/A', 'TD', 'INT',
               'SACKS', 'RUSH_ATT', 'RUSH_YDS', 'RUSH_TD', 'FL', 'G', 'FPTS', 'FPTS/G', 'OWN', 'Year']
    
    years_to_scrape = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
    df = pd.DataFrame(columns=columns)
    
    for year in years_to_scrape:
        curr_df = qb_scrape(year, columns)
        df = pd.concat([df, curr_df], ignore_index=True)
    
    df.to_csv("./StatFiles/qb_stats.csv", index=False)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] QB scraper completed!")
    return "QB scraper completed"


def run_rb_scraper():
    """Run the running back scraper and save to CSV"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting RB scraper...")
    
    columns = ['RANK', 'PLAYER', 'ATT', 'YDS', 'Y/A', 'LG', '20+', 'TD', 'REC',
               'TGT', 'REC_YDS', 'Y/R', 'REC_TD', 'FL', 'G', 'FPTS', 'FPTS/G', 'OWN', 'Year']
    
    years_to_scrape = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
    df = pd.DataFrame(columns=columns)
    
    for year in years_to_scrape:
        curr_df = rb_scrape(year, columns)
        df = pd.concat([df, curr_df], ignore_index=True)
    
    df.to_csv("./StatFiles/rb_stats.csv", index=False)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] RB scraper completed!")
    return "RB scraper completed"


def run_te_scraper():
    """Run the tight end scraper and save to CSV"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting TE scraper...")
    
    columns = ['RANK', 'PLAYER', 'REC', 'TGT', 'YDS', 'Y/R', 'LG', '20+', 'TD',
               'RUSH_ATT', 'RUSH_YDS', 'RUSH_TD', 'FL', 'G', 'FPTS', 'FPTS/G', 'OWN', 'Year']
    
    years_to_scrape = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
    df = pd.DataFrame(columns=columns)
    
    for year in years_to_scrape:
        curr_df = te_scrape(year, columns)
        df = pd.concat([df, curr_df], ignore_index=True)
    
    df.to_csv("./StatFiles/te_stats.csv", index=False)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] TE scraper completed!")
    return "TE scraper completed"


def run_wr_scraper():
    """Run the wide receiver scraper and save to CSV"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting WR scraper...")
    
    columns = ['RANK', 'PLAYER', 'REC', 'TGT', 'YDS', 'Y/R', 'LG', '20+', 'TD',
               'RUSH_ATT', 'RUSH_YDS', 'RUSH_TD', 'FL', 'G', 'FPTS', 'FPTS/G', 'OWN', 'Year']
    
    years_to_scrape = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
    df = pd.DataFrame(columns=columns)
    
    for year in years_to_scrape:
        curr_df = wr_scrape(year, columns)
        df = pd.concat([df, curr_df], ignore_index=True)
    
    df.to_csv("./StatFiles/wr_stats.csv", index=False)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] WR scraper completed!")
    return "WR scraper completed"


def main():
    """Run all scrapers concurrently"""
    print("="*60)
    print("FANTASY FOOTBALL STATS SCRAPER - CONCURRENT MODE")
    print("="*60)
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Running all position scrapers simultaneously...")
    print("-"*60)
    
    start_time = time.time()
    
    # Create a list of scraper functions
    scrapers = [run_qb_scraper, run_rb_scraper, run_te_scraper, run_wr_scraper]
    
    # Run all scrapers concurrently using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Submit all scraper tasks
        future_to_scraper = {executor.submit(scraper): scraper.__name__ for scraper in scrapers}
        
        # Wait for all tasks to complete
        for future in concurrent.futures.as_completed(future_to_scraper):
            scraper_name = future_to_scraper[future]
            try:
                result = future.result()
                print(f"✓ {result}")
            except Exception as exc:
                print(f"✗ {scraper_name} generated an exception: {exc}")
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print("-"*60)
    print(f"All scrapers completed!")
    print(f"Total execution time: {total_time:.2f} seconds")
    print(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    print("\nOutput files saved to StatFiles directory:")
    print("- qb_stats.csv")
    print("- rb_stats.csv") 
    print("- te_stats.csv")
    print("- wr_stats.csv")


if __name__ == "__main__":
    main()
