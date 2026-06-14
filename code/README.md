# AIoT Demo Code

A scenario-driven Python simulation that connects the AIoT report to a reusable
software prototype.

## Demo Features
- Scenario selection for multiple AIoT domains.
- Modular device simulation with synthetic sensor streams.
- Edge preprocessing and anomaly classification.
- Cloud baseline training and telemetry reporting.
- Human-readable narrative output for each simulation step.

## Run the demo

```bash
cd code
python3 aiot_demo.py
```

## Available scenarios
- `smart_mattress`
- `autonomous_drone`
- `security_gateway`

```bash
python3 aiot_demo.py --scenario autonomous_drone
```

## Example output behavior
- First few iterations establish a baseline from safe device readings.
- Subsequent steps perform local inference and label events.
- Anomalies are surfaced as actionable telemetry.

## Notes
- Dependency-free and compatible with standard Python 3.
- The demo is intentionally modular to support extension.
- You can enhance it with real data sources, MQTT transport, or TinyML models.

## Extension ideas
- Add JSON logging and telemetry replay.
- Build a dashboard to visualize detected anomalies.
- Integrate real hardware sensors using Raspberry Pi or microcontroller boards.
