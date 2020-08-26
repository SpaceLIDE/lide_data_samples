#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:26:29 2019

@author: camille
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# User parameters #############################################################
input_file = 'example_jitter_glider.csv'
time_min = 420 # Part of recording to be analyzed in seconds
time_max = 800
fc = 1 # Cutoff frequency of the filter 
fs = 50 # Sampling frequency in Hz
#############################################################
data = pd.read_csv(input_file)

# Part of recording to be analyzed
time = data.loc[:,"Time"]*1e-3
data_jitter_analysis = data[(data['Time']*1e-3 >= time_min + time[0]) & (data['Time']*1e-3 <= time_max + time[0])]
time = data_jitter_analysis.loc[:,"Time"]*1e-3 - time[0]

x = data_jitter_analysis.loc[:,"x"]/1000
y = data_jitter_analysis.loc[:,"y"]/1000
z = data_jitter_analysis.loc[:,"z"]/1000
norm = np.sqrt(x**2 + y**2 + z**2)

w = fc / (fs / 2) # Normalize the frequency
b, a = signal.butter(5, w, btype="highpass")
filtered_x = signal.filtfilt(b, a, x) # Filters the acceleration
filtered_y = signal.filtfilt(b, a, y) # Filters the acceleration
filtered_z = signal.filtfilt(b, a, z) # Filters the acceleration
filtered_norm = signal.filtfilt(b, a, norm) # Filters the acceleration

fig, ax1 = plt.subplots()
ax1.plot(time,norm,'r',label='Raw data')
ax1.plot(time,filtered_norm,label='High-pass filtered data')
ax1.legend()
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Acceleration [g]')
ax1.grid()
ax1.set_ylim([-0.3,1.75])
plt.title('Norm of the acceleration vector')

sigma_x = np.std(filtered_x)
print('Standard deviation of recording on X = ' + str(sigma_x))
sigma_y = np.std(filtered_y)
print('Standard deviation of recording on Y = ' + str(sigma_y))
sigma_z = np.std(filtered_z)
print('Standard deviation of recording on Z = ' + str(sigma_z))
sigma_norm = np.std(filtered_norm)
print('Standard deviation of recording on Norm = ' + str(sigma_norm))

fig, ax1 = plt.subplots()
plt.title("PSD of the norm of the acceleration vector")
plt.psd(filtered_norm, 512, fs)
ax1.set_ylim([-65,-25])
plt.show()

