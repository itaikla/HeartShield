import numpy as np
from scipy.signal import find_peaks

def process_heart_rate_data(data, sampling_rate):
    signal = np.array(data)
    
    # Assuming the data is noisy, you might want to filter it first
    # Example: Use a simple moving average filter
    window_size = 10
    filtered_signal = np.convolve(signal, np.ones(window_size) / window_size, mode='valid')
    
    # Find peaks (heartbeats) in the signal
    peaks, _ = find_peaks(filtered_signal, distance=sampling_rate * 0.5)  # Minimum distance between peaks
    
    num_peaks = len(peaks)
    duration = len(signal) / sampling_rate  # Total duration of the signal in seconds
    heart_rate_bpm = (num_peaks / duration) * 60  # Convert to beats per minute
    
    return {
        "filtered_signal": filtered_signal,
        "peaks_indices": peaks,
        "heart_rate_bpm": heart_rate_bpm
    }

def detect_heart_pulse_anomalies(heart_pulse_readings):
    # Define a threshold for heart rate variability
    threshold = 10

    anomalies = []
    for i, heart_pulse_reading in enumerate(heart_pulse_readings):
        if i > 0 and abs(heart_pulse_reading - heart_pulse_readings[i - 1]) > threshold:
            anomalies.append(i)

    return anomalies

def calculate_average_heart_rate(heart_pulse_readings):
    total_heart_beats = len(heart_pulse_readings)
    total_heart_rate = sum(heart_pulse_readings)
    average_heart_rate = total_heart_rate / total_heart_beats
    return average_heart_rate
