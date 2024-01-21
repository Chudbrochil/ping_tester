# ping_tester

### License / Why

NOTE: Feel free to use this code/repo however you wish. This project is purely for fun aside from creating some personal evidence for my ISP :)

It's subtle to detect any latency/packet loss issues with your internet. This repo can diagnose line quality issues, but also analyze your latency across time (think analyzing "peak time"). You can even run these scripts to analyze your latency to specific servers (video game servers, web hosts).

### How-to-use

The file `ping_test.py` can be ran with command line arguments on the CLI. Here are some example usages:

	python ping_test.py --filename "output" --write_cadence 30 --ping_url "www.google.com"

This would start an infinite ping test (until you hit Ctrl-C), with the file names like `output_2024-01-20.csv`, writing the csv to disk every 30s, and pinging the URL www.google.com.

Refer to ping\_analysis.ipynb for some really simple data analytics about the ping data. We can look at mean, median, quartiles, of the successful pings. Further, we can categorize the ping errors (Request Timed out, 100% packet loss).

### Sample visualizations

Here are a few example plots, visualizing latency history, and rolling average of latencies.

![image](https://github.com/Chudbrochil/ping_tester/assets/16054782/f0d02f60-3e32-4b2f-a9db-42ec24cece11)

![image](https://github.com/Chudbrochil/ping_tester/assets/16054782/87d9eb1c-4dcc-4ede-b2b0-ede81fc807a1)

