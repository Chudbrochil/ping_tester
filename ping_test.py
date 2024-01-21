import pandas as pd
import subprocess
import time
from datetime import datetime

# Function to perform a single ping and return the latency
def ping_google():
    try:
        # Pinging google.com
        response = subprocess.run(['ping', '-c', '1', 'www.google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Parsing the output for time
        output = response.stdout
        if 'time=' in output:
            latency = float(output.split('time=')[1].split(' ')[0])
        else:
            # If the ping request times out or fails, return NaN
            latency = float('nan')
        return latency
    except:
        # In case of an unexpected error, return NaN
        return float('nan')

# Function to run the ping test every second, update dataframe, and save to CSV periodically
def run_ping_test(duration_seconds, csv_filename, save_interval=10):
    # Prepare lists to store data
    times = []
    latencies = []

    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        # Get current time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Perform a ping
        latency = ping_google()
        # Store results in the lists
        times.append(current_time)
        latencies.append(latency)
        # Check if it's time to save to CSV
        if len(times) % save_interval == 0:
            # Create a dataframe and save to CSV
            df = pd.DataFrame({'Time': times, 'Latency': latencies})
            df.to_csv(csv_filename, index=False)
        # Wait for 1 second
        time.sleep(1)
    
    # Saving the final data to CSV
    df = pd.DataFrame({'Time': times, 'Latency': latencies})
    df.to_csv(csv_filename, index=False)

# Running the ping test for 30 seconds as an example and saving to 'ping_data.csv'
run_ping_test(30, 'ping_data.csv')
