# CodeAlpha AIoT Task 2

## Project Overview
This repository organizes the AIoT case study report and includes a practical
Python demo that illustrates edge/cloud data flow, sensor simulation, and
anomaly detection.

## What is included
- `AIoT_Case_Study_Report.pdf`: original case study report.
- `docs/AIoT_Case_Study_Report_Summary.md`: concise, structured summary of the report.
- `code/aiot_demo.py`: lightweight AIoT simulation demonstrating device, edge, and cloud layers.
- `code/README.md`: instructions for running and extending the demo.
- `.gitignore`: excludes Python cache artifacts.

## Report Highlights
The report explores the integration of IoT and Artificial Intelligence (AIoT) and
examines three real-world applications:
- autonomous drone delivery systems,
- physiological monitoring and smart sleep systems,
- AI-driven security and fraud detection.

It also covers the AIoT architecture:
1. Device Layer: sensors and data capture.
2. Edge/Fog Layer: local preprocessing and low-latency inference.
3. Cloud Layer: model training, analytics, and OTA updates.

## Running the Demo

```bash
cd code
python3 aiot_demo.py
```

This script simulates:
- sensor data generation,
- edge preprocessing,
- cloud baseline training,
- anomaly detection,
- telemetry payload creation.

## Repository Structure
- `code/`: executable demo and code documentation.
- `docs/`: report summary and design notes.
- `AIoT_Case_Study_Report.pdf`: original project report.

## How to Extend
- Add TinyML model inference on real sensor streams.
- Replace synthetic telemetry with MQTT or HTTP data transport.
- Implement federated learning logic for privacy-preserving edge updates.

## Goals
This repository is structured to be easy to understand and adapt. It combines
documentation, a clear code example, and a polished README so that the AIoT
report is both accessible and actionable.
