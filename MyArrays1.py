import numpy as np
import random

arr01 =  np.array([[1,2,3],
                  [4,5,6]])


arr02 = np.array([0.0,0.1,0.2,0.3,0.4])

for row in arr01:
    print(row)
    for column in row:
        print(column, end = ' ')
    print()

for i in arr01.flat:
    print(i)

arr03 = np.zeros(5)

arro04 = np.ones((2,4,), dtype=int)

arr05 = np.full((3,5), 13)


a = np.array([random.randint(1,10) for i in range(5)])

b = np.array(np.random.randint(1,10, size=(2,5)))


arr06 = np.arange(5)

arr07 = np.arange(5,10)

arr08 = np.arange(10, 1, -2)


arr09 = np.linspace(0.0, 1.0, num = 5)

arr10 = np.arange(1,21).reshape(4,5)

num01 = np.arange(1,6)

num2 = num01*2

num3 = num01**3
# this is called braodcasting** ON MIDTERM

num01 += 10 
#augmented assignment-- permanantely modifies the array

num4 = num01 * num2
#these arrays must be the same size or else there will be an error

num5 = num01 > 13

num6 = num3 > num01
#Students test scores
grades = np.array([[87,96,70], [100,87,90], [94,77,90],[100,81,82]])

print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())

#calculate average on all rows for each column
grades_by_exam = grades.mean(axis = 0)
#axis=0 -- calc average on all row for each column
# one dimensional arrray of 3 values (3 exams)


#calculate average on all columns for each row
grade_by_student = grades.mean(axis = 1)
#axis = 1 -- calc average on all columns for each row
# one dimensional array of 4 values


#Universal Functions
num7 = np.array([1,4,9,16,25,36])
num8 = np.sqrt(num7)

num9 = np.array([10,20,30,40,50,60])
num10 = np.add(num7,num9)
#num10 and num10 (below) do the smae thing, num10 is like a concatenated key
num10 = num7 + num9

num11 = np.multiply(num9, 5)
#same as 
num11 = num9 * 5
#braodacast

num12 = num9.reshape(2,3)
num13 = np.array([2,4,6])
num14 = np.multiply(num12, num13)
#Number of rows DOES NOT NEED TO MATCH UP^
#Number of columns DOES need to match

print()
