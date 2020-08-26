# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:30:34 2019

@author: gontier
"""
import analyze_data
import plot_function
import read_data

## User parameters ############################################################
# .csv files for recorded data
input_file = 'example_data_aircraft.csv'

## Post-processings ###########################################################
# Reads data
data = read_data.read_data(input_file)

# Performs various post-processings and analyzes
analyze = analyze_data.analyze_data(data)

# Plots results
plot_function.plot_function(data,analyze)