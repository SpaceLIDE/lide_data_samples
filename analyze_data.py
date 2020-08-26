# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:55:38 2019

@author: gontier
"""
import numpy as np

# Performs various post-processings and analyzes
def analyze_data(data,*args):
    
    analyze = {}
    
    altitude = data.loc[:," Alt"]
    time = data.loc[:,"Time"]
    
    # Detects summits of parabolas ############################################

    top_parabola_idx = np.where(np.diff(np.sign(np.diff(altitude)))<0)[0] + 1
    top_parabola_time = time[top_parabola_idx].values
    
    analyze["top_parabola_idx"] = top_parabola_idx
    analyze["top_parabola_time"] = top_parabola_time
    
    for i in range(top_parabola_idx.size):
        print('Summit of parabola #' + str(i) + ' reached at t=' + str(top_parabola_time[i]) + 's')
              
    ###########################################################################

    return analyze