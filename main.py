import csv
from collections import defaultdict
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from math import sqrt


def display(my_list):
    for lines in my_list:
        print(lines)
        print('\n')


def searchbyName(my_list):
    name = input("Enter the name : ")
    for li in range(len(my_list)):
        if my_list[li][1] == name:
            print(my_list[li])
            print('\n')


def DescriptiveStatistics_mean(my_List):
    sumOfGrades = 0
    for li in range(1,len(my_list)):
        sumOfGrades = sumOfGrades + int(my_list[li][3])
    mean = sumOfGrades / 10
    print(mean)


def DescriptiveStatistics_variance(my_list):
    hours = []
    score = []
    for li in range(1,len(my_list)):
        score.append(int(my_list[li][3]))
    varian=statistics.variance(score)
    print("Variance of Grades set is " + str(varian))
    Standard = sqrt(statistics.variance(score))
    print("Standard Deviation is " + str(Standard))


def CalcRegression(my_list):
    hours = []
    score = []
    for li in range(1,len(my_list)):
        hours.append(int(my_list[li][2]))
    for li in range(1,len(my_list)):
        score.append(int(my_list[li][3]))
    y = score
    x = hours
    plt.scatter(x, y)
    plt.xlabel('hours', fontsize=20)
    plt.ylabel('score', fontsize=20)
    plt.show()


def predict(my_list):
    hours = []
    score = []
    for li in range(1,len(my_list)):
        hours.append(int(my_list[li][2]))
    for li in range(1,len(my_list)):
        score.append(int(my_list[li][3]))
    y = score
    x = hours
    coordinates = [y, x]
    model = LinearRegression()
    x1 = np.array(x)
    y1 = np.array([x, y])
    model.fit(y1, y1)
    X_predict = int(input("enter the number of hours"))
    y_predict = model.predict(X_predict)
    print(y_predict)


print("         ---------Welcome---------           ")

choice = 0
file = 'SampleData.csv'
with open(file, mode='r') as f:
    csvFile = csv.reader(f)
    my_list = list(csvFile)
grade = dict()
id = []
name = []
hours = []
score = []
for li in range(1, 11):
    grade[my_list[li][0]] = my_list[li][3]

degree = dict()
for li in range(1, 11):
    grade[my_list[li][0]] = my_list[li][3]

for grad in range(1, 11):
    if int(my_list[grad][3]) >= 90:
        degree[grad] = 'A'
    elif int(my_list[grad][3]) >= 75:
        degree[grad] = 'B'
    elif int(my_list[grad][3]) > 60:
        degree[grad] = 'C'
    elif int(my_list[grad][3]) > 50:
        degree[grad] = 'D'
    else:
        degree[grad] = 'F'
flag = True
while flag:

    print('\n')
    print("Choose what you want ")
    print("1-Read File")
    print("2-Show Data ")
    print("3-Show Grades ")
    print("4-Search by name ")
    print("5-Descriptive Statistics ")
    print("6-Regression Analysis ")
    print("7-Prediction ")
    print("8-Exit ")
    choice = int(input())
    if choice == 1:
        file1 = input("Name of file")
        with open(file1, mode='r') as f:
            csvFile = csv.reader(f)
            my_list = list(csvFile)
    elif choice == 2:
        display(my_list)
    elif choice == 3:
        print(degree)
    elif choice == 4:
        searchbyName(my_list)
    elif choice == 5:
        DescriptiveStatistics_mean(my_list)
        DescriptiveStatistics_variance(my_list)
    elif choice == 6:
        CalcRegression(my_list)
    elif choice == 7:
        predict(my_list)
    elif choice == 8:
        flag =False
