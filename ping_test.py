import pandas as pd
import subprocess
import time
from datetime import datetime


# Function to perform a single ping and return the latency
def single_ping(url: str):
    # Pinging a URL we have been given (e.g. www.google.com, 8.8.8.8)
    response = subprocess.run(['ping', '-c', '1', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Parsing the output for time
    output = response.stdout
    if 'time=' in output:
        latency = float(output.split('time=')[1].split(' ')[0])
    else:
        # If the ping request times out or fails, return raw output (e.g. Request timeout for icmp_seq 0)
        latency = output
    return latency

# Dataframe writing function for our time/latency schema.
def write_pings(full_filename: str, times, latencies):

    df = pd.DataFrame({'Time': times, 'Latency': latencies})
    df.to_csv(full_filename, index=False)

# Function to run the ping test and save to a new CSV file each day
def run_ping_test_forever(filename: str, write_cadence: int = 10, ping_url: str = 'www.google.com'):
    # Initialize variables
    times = []
    latencies = []
    current_date = datetime.now().date()
    time_in_s = 0

    while True:
        # Get current time and date
        now = datetime.now()
        current_time = now.strftime('%Y-%m-%d %H:%M:%S')
        date_today = now.date()

        # If the date has rolled over, let's write the last results for the day before we start a new file.
        if date_today != current_date:
            write_pings(f'{filename}_{current_date}.csv', pd.DataFrame({'Time': times, 'Latency': latencies}))
            current_date = date_today

        if time_in_s % write_cadence == 0:
            write_pings(f'{filename}_{current_date}.csv', pd.DataFrame({'Time': times, 'Latency': latencies}))

        # Perform a ping
        latency = single_ping(ping_url)
        # Store results in the lists
        times.append(current_time)
        latencies.append(latency)

        # Wait for 1 second
        time_in_s += 1
        time.sleep(1)

run_ping_test_forever(filename="ping_data/", write_cadence=30, ping_url = 'www.google.com')


