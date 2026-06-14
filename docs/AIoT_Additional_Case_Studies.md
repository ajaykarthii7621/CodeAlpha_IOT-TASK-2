# Additional AIoT Case Studies

This document adds two new AIoT case studies that extend the original report:
Smart Grid monitoring and Air Quality Guardian systems.

## Case Study: Smart Grid Node
### Problem
Power distribution networks need to detect overloads and frequency anomalies
before they cause outages or equipment damage.

### AIoT Solution
- Edge sensors monitor voltage, current, and frequency in real time.
- Local edge AI detects voltage spikes and load surges.
- Cloud coordination helps map events across nodes for grid stability.

### Benefits
- Faster detection of power anomalies.
- Reduced risk of brownouts and blackouts.
- Better visibility into distributed grid health.

## Case Study: Air Quality Guardian
### Problem
Indoor and outdoor air quality can change quickly, affecting wellbeing and
safety.

### AIoT Solution
- Sensors continuously monitor PM2.5, CO2, and humidity.
- Edge processing filters noise and identifies dangerous spikes.
- Alerts and ventilation actions are triggered only when needed.

### Benefits
- More reliable air risk detection.
- Smarter, more efficient building ventilation.
- Better health outcomes through proactive alerts.

## How the new cases fit the AIoT architecture
- Device Layer: environmental sensors capture air and power signals.
- Edge Layer: local analytics detect hazards and reduce false alarms.
- Cloud Layer: aggregated trend analysis and adaptive update rules.

## Connection to the demo
The new scenarios are implemented in `code/aiot_demo.py` as:
- `smart_grid`
- `air_quality_guardian`

Use these scenarios to explore new AIoT domains and extend the prototype.
