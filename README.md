# Network Intelligence Lab

Experiments and prototypes exploring how network telemetry, RF engineering data and AI techniques can be combined to improve telecom network troubleshooting and optimization.

## Motivation

Modern wireless networks generate enormous volumes of telemetry including KPI statistics, alarms, configuration parameters and drive-test measurements. Engineers must translate this raw data into actionable insights about coverage, interference, mobility and capacity.

This repository explores approaches for transforming raw network telemetry into structured engineering intelligence using automation, data analysis and AI-assisted workflows.

## Focus Areas

• Telecom telemetry pipelines  
• KPI anomaly detection  
• Outage-to-performance correlation  
• RF hotspot detection and ranking  
• Geospatial network performance analysis  
• AI-assisted troubleshooting workflows  
• Retrieval-augmented knowledge systems for engineering documentation  

## Example Use Cases

• Detecting abnormal KPI patterns across large networks  
• Ranking network trouble spots using multiple performance indicators  
• Correlating outage reports with network telemetry  
• Supporting RF engineers with automated troubleshooting guidance  

## Technologies Used

Python  
SQL  
Network telemetry analytics  
LLM workflows  
RAG (retrieval augmented generation)  
Automation tools and APIs  

## Future Work

Future experiments will explore:

• ML-based anomaly detection in network KPI data  
• Automated RF troubleshooting assistants  
• AI-supported network operations workflows  
• ORAN-style analytics and decision support systems  

## Author

Jeff Taylor  
Principal RF / Network Intelligence Engineer

## Example Scripts

### telemetry_hotspot_detector.py

A simple prototype illustrating how telecom KPI data can be analyzed to detect potential network hotspots using rule-based logic.

The script demonstrates how engineers might combine:

• Drop call rate  
• SINR measurements  
• Throughput statistics  

to identify potential network trouble spots across multiple sites.

## Example Scripts and Notebooks

### telemetry_hotspot_detector.py
A simple prototype illustrating how telecom KPI data can be analyzed to detect potential network hotspots using rule-based logic.

### kpi_anomaly_detection_demo.ipynb
A notebook demonstrating basic KPI anomaly detection using hourly telecom performance data, threshold-based logic and a throughput visualization.
