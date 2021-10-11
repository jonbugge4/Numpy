import numpy as np
#Rows - Each Student (Student0, Student1, Student2, Student3)
#Columns - Each Test (Test0, Test1, Test 2)
grades = np.array([[87,96,70], [100,87,90], [94,77,90],[100,81,82]])

student1 = grades[1]

#row, column
student0_Test1 = grades[0,1]

#Upper bound is not included so we do 2 instead of 1
students0_1 = grades[0:2]

#double brackets represent just rows, not columns allows us to grab two students
student1and3 = grades[[1,3]]


#grades[row,column]
#grades[[1,3], 2]
student1and3_test2 = grades[[1,3],2]

#just doing a collen, python knows to grab upper and lower bound
allstudents_tes1 = grades[:,0]

all_students_test1_2 = grades[:, 1:3]

all_students_test0_2 = grades[:,[0,2]]

import random
grades = np.random.randint(60, 101, 12).reshape(3,4)

grades.mean()

#average by test-score (column)
grades.mean(axis=0)

#average by student (row)
grades.mean(axis = 1)

numbers = np.arange(1,6)


#shallow copy
numbers_view = numbers.view()

numbers[1] *= 10

numbers_view[1] /= 10

number_slice = numbers[0:3]

numbers[1] *= 20

#Deep Copies- changes to the orginial does NOT affect the deep copy

numbers_copy = numbers.copy()

numbers[1] *= 10

#reshape method produces a shallow copy
grades = np.array ([[87,96,70],[100,87,90]])
grades_reshaped = grades.reshape(1,6)

#resize method changes the original array
grades.resize(1,6)


#flatten creates a deep copy
flattened = grades.flatten()

#raveled creates a shallow copy
raveled = grades.ravel()
raveled[0] = 100
flattened[1] = 100


grades = np.array ([[87,96,70],[100,87,90]])

grades.T

grades2 = np.array([[94,77,90], [100,81,82]])

h_grades = np.hstack((grades, grades2))

v_grades = np.vstack((grades, grades2))




print()