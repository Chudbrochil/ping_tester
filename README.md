# ping_tester

### Why

It's subtle to detect any latency/packet loss issues with your internet. This repo can diagnose line quality issues, but also analyze your latency across time (think analyzing "peak time"). You can even run these scripts to analyze your latency to specific servers (video game servers, web hosts).

### How-to-use

The file `ping_test.py` can be ran with command line arguments on the CLI. Here are some example usages:

	python ping_test.py --filename "output" --write_cadence 30 --ping_url "www.google.com"

This would start an infinite ping test (until you hit Ctrl-C), with the file names like `output_2024-01-20.csv`, writing the csv to disk every 30s, and pinging the URL www.google.com.

Refer to ping\_analysis.ipynb for some really simple data analytics about the ping data. We can look at mean, median, quartiles, of the successful pings. Further, we can categorize the ping errors (Request Timed out, 100% packet loss).

### Sample visualizations

Here are a few example plots.

Latency raw history (over a whole day)

![image](https://github.com/Chudbrochil/ping_tester/assets/16054782/e8e7bfe6-ddbc-4c01-bea5-6335e6a4b4ea)

Rolling average of latency

![image](https://github.com/Chudbrochil/ping_tester/assets/16054782/8fb9a3ef-a006-41d1-a0a8-4354091d08f7)

Boxplot of latency, with 95% outliers removed.

![image](https://github.com/Chudbrochil/ping_tester/assets/16054782/0871f768-ab17-44c5-84db-543646ca1b80)

Anomaly detection (IsolationForest)

![image](https://github.com/Chudbrochil/ping_tester/assets/16054782/5edd3dc1-51ef-4716-9d61-a60cd8ff6eb0)
















