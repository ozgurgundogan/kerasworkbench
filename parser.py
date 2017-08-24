from numpy import genfromtxt
import glob
import os

fileNames = []
os.chdir(".")
for f in glob.glob("*.txt"):
    fileNames.append(f)


def getASetOfData():
    if(len(fileNames) == 0):
        return
    f = fileNames[0]
    fileNames.remove(f)
    my_data = genfromtxt(f, delimiter='\n')
    print my_data.size
    return my_data


for l in range(len(fileNames)):
    getASetOfData()
# for root, dirs, files in os.walk(r"C:\Users\hilmi\Desktop\keras/"):  # directory
#     for f in files:  # files in directory
#         my_data = genfromtxt('f', delimiter='\n')
#         print my_data.size
