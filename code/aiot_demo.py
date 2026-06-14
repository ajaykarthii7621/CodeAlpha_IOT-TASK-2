"""
AIoT Demo: Scenario-Based Edge and Cloud Simulation

This script demonstrates multiple AIoT scenarios with modular device profiles,
edge inference, and cloud-style baseline learning. It is intentionally designed
for clarity, storytelling, and future extension.
"""

from dataclasses import dataclass, field
import argparse
import json
import random
import statistics
import time
from typing import Any, Dict, List


@dataclass
class DeviceScenario:
    name: str
    sensors: List[str]
    safe_ranges: Dict[str, tuple]
    anomaly_models: Dict[str, Dict[str, Any]]
    history: List[Dict[str, float]] = field(default_factory=list)

    def generate_reading(self) -> Dict[str, float]:
        reading = {}
        for sensor in self.sensors:
            minimum, maximum = self.safe_ranges[sensor]
            value = random.uniform(minimum, maximum)
            if random.random() < self.anomaly_models[sensor]['chance']:
                offset = random.uniform(*self.anomaly_models[sensor]['spike'])
                value += offset
            reading[sensor] = round(value, 3)
        return reading


SCENARIOS = {
    'smart_mattress': DeviceScenario(
        name='Smart Mattress',
        sensors=['temperature_c', 'heart_rate_bpm', 'motion_index'],
        safe_ranges={
            'temperature_c': (22.0, 26.0),
            'heart_rate_bpm': (55.0, 75.0),
            'motion_index': (0.0, 0.4),
        },
        anomaly_models={
            'temperature_c': {'chance': 0.08, 'spike': (4.0, 9.0)},
            'heart_rate_bpm': {'chance': 0.06, 'spike': (20.0, 40.0)},
            'motion_index': {'chance': 0.05, 'spike': (0.8, 1.5)},
        },
    ),
    'autonomous_drone': DeviceScenario(
        name='Autonomous Drone',
        sensors=['battery_pct', 'obstacle_distance_m', 'gps_accuracy_m'],
        safe_ranges={
            'battery_pct': (60.0, 100.0),
            'obstacle_distance_m': (5.0, 20.0),
            'gps_accuracy_m': (0.5, 2.0),
        },
        anomaly_models={
            'battery_pct': {'chance': 0.05, 'spike': (-40.0, -25.0)},
            'obstacle_distance_m': {'chance': 0.06, 'spike': (-4.0, -2.0)},
            'gps_accuracy_m': {'chance': 0.04, 'spike': (3.0, 7.0)},
        },
    ),
    'security_gateway': DeviceScenario(
        name='Security Gateway',
        sensors=['auth_score', 'audio_energy', 'stability_index'],
        safe_ranges={
            'auth_score': (0.7, 1.0),
            'audio_energy': (20.0, 40.0),
            'stability_index': (0.8, 1.0),
        },
        anomaly_models={
            'auth_score': {'chance': 0.07, 'spike': (-0.6, -0.4)},
            'audio_energy': {'chance': 0.05, 'spike': (15.0, 30.0)},
            'stability_index': {'chance': 0.04, 'spike': (-0.5, -0.3)},
        },
    ),
}


def preprocess(reading: Dict[str, float]) -> Dict[str, float]:
    cleaned = {key: round(value, 3) for key, value in reading.items()}
    return cleaned


def train_cloud_baseline(history: List[Dict[str, float]]) -> Dict[str, Dict[str, float]]:
    baseline = {}
    if not history:
        return baseline
    for key in history[0].keys():
        values = [entry[key] for entry in history]
        baseline[key] = {
            'mean': statistics.mean(values),
            'stdev': statistics.stdev(values) if len(values) > 1 else 0.1,
        }
    return baseline


def infer_edge(reading: Dict[str, float], baseline: Dict[str, Dict[str, float]]) -> List[str]:
    anomalies = []
    for key, stats in baseline.items():
        if stats['stdev'] <= 0:
            continue
        z_score = abs((reading[key] - stats['mean']) / stats['stdev'])
        if z_score > 2.2:
            anomalies.append(f'{key} ({reading[key]} | z={z_score:.2f})')
    return anomalies


def format_telemetry(scenario: DeviceScenario, reading: Dict[str, float], anomalies: List[str]) -> Dict[str, Any]:
    payload = {
        'scenario': scenario.name,
        'timestamp': time.time(),
        'sensor_data': reading,
        'status': 'ALERT' if anomalies else 'STABLE',
        'anomaly_count': len(anomalies),
        'anomaly_details': anomalies,
    }
    return payload


def run_simulation(scenario_key: str, steps: int = 24, warmup: int = 6):
    scenario = SCENARIOS[scenario_key]
    print(f'AIoT Scenario: {scenario.name}\n')
    print('Initializing device profile...')
    print(f'- Sensors: {scenario.sensors}')
    print(f'- Warmup phase: {warmup} steps to build baseline\n')

    for step in range(1, steps + 1):
        raw_reading = scenario.generate_reading()
        local_reading = preprocess(raw_reading)

        scenario.history.append(local_reading)
        if len(scenario.history) < warmup:
            print(f'[STEP {step}] Baseline warmup: {local_reading}')
            continue

        baseline = train_cloud_baseline(scenario.history[-warmup:])
        anomalies = infer_edge(local_reading, baseline)
        telemetry = format_telemetry(scenario, local_reading, anomalies)

        print(f'[STEP {step}] Edge inference => {telemetry["status"]}')
        print(f'           Sensor data: {local_reading}')
        if anomalies:
            print(f'           Detected: {anomalies}\n')
        else:
            print('           No anomalies detected.\n')

    summary = {
        'scenario': scenario.name,
        'total_steps': steps,
        'alerts': sum(1 for i in range(warmup, steps) if infer_edge(scenario.history[i], train_cloud_baseline(scenario.history[max(0, i - warmup + 1):i + 1]))),
        'final_baseline': train_cloud_baseline(scenario.history[-warmup:]),
    }
    print('Simulation complete. Summary:')
    print(json.dumps(summary, indent=2))
    return summary


def parse_arguments():
    parser = argparse.ArgumentParser(description='AIoT scenario simulation.')
    parser.add_argument('--scenario', choices=SCENARIOS.keys(), default='smart_mattress')
    parser.add_argument('--steps', type=int, default=24)
    parser.add_argument('--warmup', type=int, default=6)
    return parser.parse_args()


def main():
    args = parse_arguments()
    run_simulation(args.scenario, steps=args.steps, warmup=args.warmup)


if __name__ == '__main__':
    main()
