from numpy import genfromtxt


for root, dirs, files in os.walk(r"C:\Users\hilmi\Desktop\keras/"):  # directory
    for f in files:  # files in directory
        my_data = genfromtxt('f', delimiter='\n')
        print my_data.size
