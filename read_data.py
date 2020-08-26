# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:43:52 2019

@author: gontier
"""

import pandas as pd

# Uses the pandas library to read recorded data from GPS, Gyro and
# accelerometer from .csv files
def read_data(input_file):

    data = pd.read_csv(input_file)
    data = data[data.loc[:," Alt"] != 0]
    data = data[data.loc[:," Lat"] != 0]
    data = data[data.loc[:," Lon"] != 0]
    data = data[data.loc[:," Vel"] != 0]
    data = data[data.loc[:," Nsat"] != 0]
    data = data.reset_index(drop=True)
    return data

