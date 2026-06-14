# AIoT Demo Code

A scenario-driven Python prototype that brings the case study into a working
simulation. The demo models device behavior, edge inference, and cloud-style
analytics.

## Demo Features
- Scenario selection for three AIoT domains.
- Synthetic sensor generation with anomaly injection.
- Edge data preprocessing and z-score anomaly detection.
- Cloud baseline learning from recent history.
- Actionable telemetry that mimics real AIoT alerts.

## Run the demo

```bash
cd code
python3 aiot_demo.py
```

## Available scenarios
| Scenario | Description |
|---|---|
| `smart_mattress` | Simulates sleep monitoring and physiological alerts |
| `autonomous_drone` | Simulates drone health and obstacle-risk signals |
| `security_gateway` | Simulates trust scoring and threat detection|

### Run a scenario
```bash
python3 aiot_demo.py --scenario autonomous_drone
```

### Customize your simulation
```bash
python3 aiot_demo.py --scenario smart_mattress --steps 40 --warmup 8
```

## Demo behavior
- Early warmup steps build a baseline from healthy readings.
- Later steps use edge inference to detect anomalies in real time.
- Telemetry payloads include status, anomaly count, and event details.

## Creative uses
- Use this demo as a template for smart health prototypes.
- Extend it for drone diagnostics or security edge gateways.
- Add data visualization to turn the simulation into a dashboard.

## Notes
- Runs with standard Python 3, no extra packages required.
- Designed to be extended into a real AIoT proof of concept.
- Ideal for students, designers, and developers learning AIoT.
