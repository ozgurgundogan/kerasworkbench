from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation
import keras
from keras.layers import Input
from keras.optimizers import SGD

import os
import numpy as np
from numpy import genfromtxt

model = Sequential()
model.add(Dense(10000,input_dim=80000))
model.add(Activation('relu'))
model.add(Dense(2000))
model.add(Activation('relu'))
model.add(Dense(300))
model.add(Activation('relu'))
model.add(Dense(3))

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
            my_data = genfromtxt(file, delimiter='\n')
            print (my_data.size) 

            model.compile(loss='mse', optimizer = 'rmsprop',metrics = ['accuracy'])
            model.fit(my_data,ground_truth,epochs = 1, batch_size = 1)
