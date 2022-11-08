import pandas as pd
import numpy as np

data =  pd.read_csv('C:/Users/snake/OneDrive/Documents/GitHub/cs2900-python-ToddJewellMyers/Projects/Project2/id-hw-exams.csv')
data2 =  pd.read_csv('C:/Users/snake/OneDrive/Documents/GitHub/cs2900-python-ToddJewellMyers/Projects/Project2/id-section.csv')

data3 = pd.concat([data, data2])

data3 = data3.drop(columns='Homework 1 - Submission Time')
data3 = data3.drop(columns='Homework 2 - Submission Time')
data3 = data3.drop(columns='Homework 3 - Submission Time')
data3 = data3.drop(columns='Homework 4 - Submission Time')
data3 = data3.drop(columns='Homework 5 - Submission Time')
data3 = data3.drop(columns='Homework 6 - Submission Time')
data3 = data3.drop(columns='Homework 7 - Submission Time')
data3 = data3.drop(columns='Homework 8 - Submission Time')
data3 = data3.drop(columns='Homework 9 - Submission Time')
data3 = data3.drop(columns='Homework 10 - Submission Time')
data3 = data3.drop(columns='Exam 1 - Submission Time')
data3 = data3.drop(columns='Exam 2 - Submission Time')
data3 = data3.drop(columns='Exam 3 - Submission Time')

data3 = data3.fillna(0)

print(data3)