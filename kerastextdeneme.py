import os
import numpy as np


def remove_zero(s):
    return s[:-1]

for root, dirs, files in os.walk(r"C:\Users\hilmi\Desktop\keras/"): #directory
    for file in files:  #files in directory
        if file.endswith(".txt"): # finding .txt files
            a,b,c = file.split('_')  #extracting ground truth
            g1 =float(a)
            g2 =float(b)
            if c.endswith('.txt'):
                g3 = float(c[:-4])
            ground_truth = np.array([g1,g2,g3]) # ground truth we obtain from .txt
            with open(file,'r') as f:
                data = f.read().replace('\n','')
                splitted_data = data.split('.')
                results = [remove_zero(s) for s in splitted_data]
                results.pop(0)
                last_form = ["0." + result for result in results]
                
float_data = [float(element) for element in last_form]
print(float_data)
