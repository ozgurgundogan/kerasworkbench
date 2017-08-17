import os
import numpy as np

data = np.array([])
for root, dirs, files in os.walk(r"C:\Users\hilmi\Desktop\keras/"): #directory
    for file in files:  #files in directory
        if file.endswith(".txt"): # finding .txt files
            a,b,c = file.split('_')  #extracting ground truth
            g1 =float(a)
            g2 =float(b)
            if c.endswith('.txt'):
                g3 = float(c[:-4])
            ground_truth = np.array([g1,g2,g3]) # ground truth we obtain from .txt
            with open(file) as f:
                for line in f: # reading line by line
                    data = np.append(data,line) #filling numpy array
float_data = [float(element) for element in data]
print(float_data[0]) #test 

