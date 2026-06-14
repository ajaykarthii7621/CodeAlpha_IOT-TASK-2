"""
AIoT Demo: Edge and Cloud Simulation

This demo simulates a simple Artificial Intelligence of Things (AIoT) pipeline.
It generates synthetic sensor data, processes it at the edge, detect anomalies
locally, and simulates a cloud-based model update.

Key concepts in this repository:
- Device Layer: sensor generation and raw signal capture
- Edge Layer: preprocessing, noise filtering, local inference
- Cloud Layer: model training, global intelligence, OTA updates
"""

import random
import statistics
import time


def simulate_sensor_data(sample_count=30):
    """Generate synthetic multisensor readings."""
    for _ in range(sample_count):
        data = {
            'temperature_c': round(random.uniform(20.0, 30.0), 2),
            'heart_rate_bpm': round(random.uniform(55.0, 95.0), 1),
            'motion_index': round(random.uniform(0.0, 1.0), 3),
        }
        if random.random() < 0.08:
            data['temperature_c'] += random.uniform(5.0, 10.0)
        if random.random() < 0.06:
            data['heart_rate_bpm'] += random.uniform(25.0, 45.0)
        if random.random() < 0.05:
            data['motion_index'] += random.uniform(1.0, 2.0)
        yield data


def edge_preprocess(sample):
    """Simulate edge preprocessing and noise reduction."""
    result = sample.copy()
    result['temperature_c'] = round(result['temperature_c'], 2)
    result['heart_rate_bpm'] = round(result['heart_rate_bpm'], 1)
    result['motion_index'] = round(min(result['motion_index'], 3.0), 3)
    return result


def cloud_train_baseline(history):
    """Simulate cloud training using aggregated edge data."""
    baseline = {}
    for key in history[0].keys():
        values = [sample[key] for sample in history]
        baseline[key] = {
            'mean': statistics.mean(values),
            'stdev': statistics.stdev(values) if len(values) > 1 else 0.1,
        }
    return baseline


def edge_inference(sample, baseline, z_threshold=2.0):
    """Run a simple edge anomaly detector using baseline z-scores."""
    anomalies = []
    for key, stats in baseline.items():
        if stats['stdev'] <= 0:
            continue
        z_score = abs((sample[key] - stats['mean']) / stats['stdev'])
        if z_score > z_threshold:
            anomalies.append((key, sample[key], round(z_score, 2)))
    return anomalies


def publish_telemetry(sample, anomalies):
    """Simulate telemetry publishing from the edge to the cloud."""
    status = 'ALERT' if anomalies else 'OK'
    payload = {
        'sensor_data': sample,
        'status': status,
        'anomaly_count': len(anomalies),
    }
    return payload


def main():
    print('AIoT Demo: Simulated device -> edge -> cloud pipeline')
    history = []

    for step, raw_sample in enumerate(simulate_sensor_data(), 1):
        edge_sample = edge_preprocess(raw_sample)
        history.append(edge_sample)

        if step < 5:
            print(f'[STEP {step}] Collecting baseline data: {edge_sample}')
        else:
            baseline = cloud_train_baseline(history[-10:])
            anomalies = edge_inference(edge_sample, baseline)
            message = publish_telemetry(edge_sample, anomalies)
            print(f'[STEP {step}] Edge inference: {edge_sample}')
            print(f'           Telemetry: {message}')
            if anomalies:
                print(f'           Detected anomalies: {anomalies}')

        time.sleep(0.1)

    print('\nDemo complete. This example mirrors the AIoT report architecture:')
    print('- Device Layer: synthetic sensors')
    print('- Edge Layer: preprocessing + inference')
    print('- Cloud Layer: baseline training and intelligence')


if __name__ == '__main__':
    main()
