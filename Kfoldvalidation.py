# K-fold validation
import csv
import math
import random
import numpy

def readcsv(filename):
    f = open(filename ,'r')
    ReaderObj = csv.reader(f)
    dataset = list(ReaderObj)
    return dataset

def str_to_float(dataset):
    for rowElem in dataset:
        for column in range(len(dataset[0])):
            #rowElem[column] = float(rowElem[column]) --> also works
            rowElem[column] = float(rowElem[column].strip())






#main
#filename = 'C:\\Users\\Parul\\Dropbox\\PythonPractice\\diabetes.csv'
#datasetTemp = readcsv(filename)
#print(datasetTemp[1])
#dataset = datasetTemp[1:]
#print(dataset[1])
#str_to_float(dataset)
#print(dataset[1])


random.seed(1)
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]


# K-fold cross validation
# divide the data into chunks
K = 4
LenDataset = len(dataset)
LenSubDataset = int(math.floor(LenDataset/K))
#print(LenSubDataset)

Subdataset = []
datasetCopy = list(dataset)  # creating folds without replacement/ disjointed
for i_K in range (K):
    FoldDataset = []
    for i_sub in range (LenSubDataset):
        i_randIdx = random.randrange(len(datasetCopy))
        #print(i_randIdx)
        #print(dataset.pop(i_randIdx))
        subdatasetTemp = datasetCopy.pop(i_randIdx)
        #subdatasetTemp = dataset[i_randIdx] <--- NOT correct
        #print(dataset[i_randIdx])
        #print(dataset.pop(i_randIdx))
        FoldDataset.append(subdatasetTemp)
    Subdataset.append(FoldDataset)
#print(FoldDataset[0])
print(Subdataset)
