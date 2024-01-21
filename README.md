# ping_tester

Fun project to test my ISPs line quality.

The file `ping_test.py` can be ran with command line arguments on the CLI. Here are some example usages:

	python ping_test.py --filename "output" --write_cadence 30 --ping_url "www.google.com"

This would start an infinite ping test (until you hit Ctrl-C), with the file names like `output_2024-01-20.csv`, writing the csv to disk every 30s, and pinging the URL www.google.com.

Refer to ping\_analysis.ipynb for some really simple data analytics about the ping data. We can look at mean, median, quartiles, of the successful pings. Further, we can categorize the ping errors (Request Timed out, 100% packet loss).


