# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:19:18 2019

@author: gontier
"""
import matplotlib.pyplot as plt
import numpy as np

# Plots results
def plot_function(data,analyze):
    
    g = 9.80665
    altitude = data.loc[:," Alt"]/100
    time = data.loc[:,"Time"]
    time = time - time[0]
    longitude = data.loc[:," Lon"]*1e-7
    latitude = data.loc[:," Lat"]*1e-7
    gForce_x = data.loc[:," a_x"]/g
    gForce_y = data.loc[:," a_y"]/g
    gForce_z = data.loc[:," a_z"]/g
    acc_norm = np.sqrt(gForce_x**2 + gForce_y**2 + gForce_z**2)
    
    ## Figure 1: altitude and vertical acceleration as functions of time ##############################
    
    fig, ax1 = plt.subplots()
    ax1.plot(time, acc_norm,'r')
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('G force [g]', color='r')
    ax1.tick_params('y', colors='r')
    ax1.grid()
    ax2 = ax1.twinx()
    ax2.plot(time, altitude, 'b')
    ax2.set_ylabel('Altitude [m]', color='b')
    ax2.tick_params('y', colors='b')
    ax2.grid()
    fig.tight_layout()
    plt.title('Altitude and norm of proper acceleration')
    
    fig, ax1 = plt.subplots()
    ax1.plot(time, gForce_x,'r')
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('G force [g]', color='r')
    ax1.grid()
    plt.title('X axis proper acceleration')

    fig, ax1 = plt.subplots()
    ax1.plot(time, gForce_y,'r')
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('G force [g]', color='r')
    ax1.grid()
    plt.title('Y axis proper acceleration')
    
    fig, ax1 = plt.subplots()
    ax1.plot(time, gForce_z,'r')
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('G force [g]', color='r')
    ax1.grid()
    plt.title('Z axis proper acceleration')
    
    ## Figure 2: glider trajectory ##############################

    fig, ax1 = plt.subplots()
    ax1.plot(longitude,latitude)
    ax1.set_ylabel('Latitude [deg]')
    ax1.set_xlabel('Longitude [deg]')
    ax1.grid()
    plt.title('Trajectory')