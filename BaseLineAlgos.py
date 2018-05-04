# Scale Machine Learning Data
# Normalization

import csv
import numpy

# read a csv file
def readcsv(filename):
    file  = open(filename, 'r')
    h = csv.reader(file)
    lines = list()
    for row in h:
        if not row:
            continue
        lines.append(row)
    return lines

# convert a column to float
def string_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


def find_min_max(dataset, column):
    element = [row[column] for row in dataset]
    maxVal = max(element)
    minVal = min(element)
    return [minVal, maxVal]


def find_mean_std(dataset, column):
    element = [row[column] for row in dataset]
    meanVal = numpy.mean(element)
    stdVal = numpy.std(element)
    return [meanVal, stdVal]

# normalization
def normalization(dataset, min_max_val):
    for row in dataset:
        for i in range(len(row)):
           row[i] = (row[i] - min_max_val[i][0])/(min_max_val[i][1]-min_max_val[i][0])

# normalization
def standardization(dataset, mean_std_Val):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - mean_std_Val[i][0]) / (mean_std_Val[i][1])


# main
filename = 'C:\\Users\\Parul\\Dropbox\\PythonPractice\\diabetes.csv'
datasetTemp = readcsv(filename)

# removing the first row of dataset
# See both datasetTemp and dataset point to the same location
dataset = datasetTemp[1:]

# Pre-processing
for column in range(len(dataset[0])):
    string_to_float(dataset, column)
#print(dataset[0])


# normalization
min_max_val = []
for column in range(len(dataset[0])):
    output = find_min_max(dataset, column)
    min_max_val.append(output)
#print(min_max_val)


# standardization
mean_std_val = []
for column in range(len(dataset[0])):
    output2 = find_mean_std(dataset, column)
    mean_std_val.append(output2)

#normalization(dataset, min_max_val)
standardization(dataset, mean_std_val)
print(dataset[0])
#print('\n')
#print(dataset[0])



#List1 = [1,2,3,4]
#print(List1[0])
#print(List1[2])
#print(List1[1:])
#print(List1[0:2])
#print(List1[0:-1])


List2 = [[1,2,3],[4,5,6]]
#print(List2)
#print(List2[1][-1])
