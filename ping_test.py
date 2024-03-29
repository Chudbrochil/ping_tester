import pandas as pd
import subprocess
import time
from datetime import datetime
import argparse
import os

# Function to ping a URL once and return the latency
def single_ping(url: str):
    response = subprocess.run(['ping', '-c', '1', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = response.stdout
    if 'time=' in output:
        latency = float(output.split('time=')[1].split(' ')[0])
    else:
        latency = output
    return latency

# Function to write the ping data to a CSV file
def write_pings(full_filename: str, times, latencies):
    df = pd.DataFrame({'Time (s)': times, 'Latency (in ms)': latencies})
    if os.path.exists(full_filename):
        df.to_csv(full_filename, mode='a', header=False, index=False)
    else:
        df.to_csv(full_filename, mode='w', header=True, index=False)

# "Main function" used to run the ping test, while writing data to a CSV file for further data analysis.
def run_ping_test_forever(filename: str, write_cadence: int, ping_url: str):
    times = []
    latencies = []
    current_date = datetime.now().date()
    time_in_s = 0

    while True:
        now = datetime.now()
        current_time = now.strftime('%Y-%m-%d %H:%M:%S')
        date_today = now.date()

        # We will reset the dataframe every time that we hit the write_cadence or that we roll over to a new day.
        if (date_today != current_date) or (time_in_s % write_cadence == 0):
            write_pings(f'{filename}_{current_date}.csv', times, latencies)
            times = []
            latencies = []
            current_date = date_today

        latency = single_ping(ping_url)
        times.append(current_time)
        latencies.append(latency)

        time_in_s += 1
        time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description='Run a continuous ping test and log results to a CSV file.')
    parser.add_argument('--filename', type=str, default='ping_data/', help='Base filename for the CSV files.')
    parser.add_argument('--write_cadence', type=int, default=30, help='Interval in seconds for writing data to CSV.')
    parser.add_argument('--ping_url', type=str, default='www.google.com', help='URL to ping.')

    args = parser.parse_args()

    run_ping_test_forever(filename=args.filename, write_cadence=args.write_cadence, ping_url=args.ping_url)

if __name__ == '__main__':
    main()
