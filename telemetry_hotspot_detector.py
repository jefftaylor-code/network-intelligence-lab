"""
Network Intelligence Lab
Example: Simple KPI hotspot detection

This script demonstrates a simple way to analyze telecom KPI data
and identify potential network trouble spots based on threshold rules.

In real networks, these KPIs might include:
- RSRP
- SINR
- Drop Call Rate
- Throughput
- Accessibility
"""

import pandas as pd

# Example dataset
data = {
    "site_id": ["SEA001", "SEA002", "SEA003", "SEA004", "SEA005"],
    "drop_call_rate": [0.8, 3.5, 1.2, 5.1, 0.4],
    "avg_sinr": [22, 9, 18, 7, 25],
    "avg_throughput_mbps": [85, 22, 60, 18, 92]
}

df = pd.DataFrame(data)

# Simple rules for identifying hotspots
DROP_RATE_THRESHOLD = 3.0
SINR_THRESHOLD = 10
THROUGHPUT_THRESHOLD = 25

def detect_hotspots(df):
    hotspots = df[
        (df["drop_call_rate"] > DROP_RATE_THRESHOLD) |
        (df["avg_sinr"] < SINR_THRESHOLD) |
        (df["avg_throughput_mbps"] < THROUGHPUT_THRESHOLD)
    ]
    return hotspots

hotspots = detect_hotspots(df)

print("Potential Network Hotspots:")
print(hotspots)
