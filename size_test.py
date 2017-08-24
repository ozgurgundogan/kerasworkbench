from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation
import keras
from keras.layers import Input
from keras.optimizers import SGD

import os
import numpy as np
from numpy import genfromtxt

model = Sequential()
model.add(Dense(10000, input_dim = 80000))
model.add(Activation('relu'))
model.add(Dense(2000))
model.add(Activation('relu'))
model.add(Dense(300))
model.add(Activation('relu'))
model.add(Dense(3, activation='relu'))

my_input_matrix = np.zeros(shape=(630,80000))
ground_truth_matrix = np.zeros(shape=(630,3))
i = 0
for root, dirs, files in os.walk(r"C:\Users\hilmi\Desktop\keras/"):
    for ff in files:
        if ff.endswith(".txt"):
            a,b,c = ff.split('_')  #extracting ground truth
            g1 =float(a)
            g2 =float(b)
            if c.endswith('.txt'):
                g3 = float(c[:-4])
            ground_truth_matrix[i] = np.array([g1,g2,g3])
            my_input_matrix[i] = genfromtxt(r"C:\Users\hilmi\Desktop\keras/" + ff, delimiter='\n')
            i = i+1
           
print(my_input_matrix.shape)
print(ground_truth_matrix.shape)
# stochastic gradient descent            
sgd = keras.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
            
model.compile(loss='mse', optimizer = sgd ,metrics = ['accuracy'])
histry = model.fit(my_input_matrix,ground_truth_matrix,epochs = 1, batch_size = 1,validation_split =0.13, verbose=2)
print (histry)
