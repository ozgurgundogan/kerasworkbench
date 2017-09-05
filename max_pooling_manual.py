import os
import numpy as np
from numpy import genfromtxt

def maxPoolManual(input_matrix,k):
    pooled_array = np.empty(int(80000/k),dtype=float)
    for a in range(0,80000,k):
        pooled_array[int(a/k)] = max(input_matrix[a:a+k-1])
    return pooled_array 
