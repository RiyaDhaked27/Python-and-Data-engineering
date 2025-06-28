# ****************************************** Assignment 8 ******************************************

import numpy as np
print(np.__version__)

# >>>>>>>>>>>>>>>>>>>>>>>> Question 1 >>>>>>>>>>>>>>>>>>>>>>>>>>
# combine 1D and 2D Numpy array :
arr1 = np.array([45,36,23,89,90])
print("1D array is:\n",arr1)
arr2 = np.array([[4,6,8],[5,7,1], [10,20,30]])
print("2D array is:\n",arr2)

# for combining use flatten on 2D array :
print("\nafter combining 1D and 2D array using flatten():\n", np.concatenate((arr1, arr2.flatten())))

# for combining use reshape(change in 1D array) of 2D array :
new_2d = np.reshape(arr2, (-1))
print("\nnow after reshape of 2D array is:\n", new_2d)
print("\nafter combining 1D and new 2D array:\n", np.concatenate((arr1, new_2d)))

# >>>>>>>>>>>>>>>>>>>>>>>> Question 2 >>>>>>>>>>>>>>>>>>>>>>>>>>
arr2 = np.array([[40,60,80],[50,70,10], [100,200,300], [24,34,56]])
print("\n2D array is:\n",arr2)
print("after flatten():\n", arr2.flatten())

# >>>>>>>>>>>>>>>>>>>>>>>> Question 3 >>>>>>>>>>>>>>>>>>>>>>>>>>
arr2 = np.array([[40,60,80],[50,70,10], [100,200,300], [24,34,56]])
print("\n2D array is:\n",arr2)
print("reverse of 2D array:\n", np.flip(arr2))

# >>>>>>>>>>>>>>>>>>>>>>>> Question 4 >>>>>>>>>>>>>>>>>>>>>>>>>>

arr = np.array([[40,60,80],[50,70,10], [100,200,300], [24,34,56]])
print("\n2D array is:\n",arr)

# max value :
maximum = np.max(arr)
print("\nmaximum value from 2D array:\n", maximum)

# min value :
minimum = np.min(arr)
print("\nminimum value from 2D array:\n", minimum)

# no. of column and row is :
res = arr.shape
print("\nno. of column and row is:\n", res)

# print specific element :
res = arr[1]
res1 = arr[(0,1),1]                                     # print the element of both 0th index row and 1st index row which is present at 1st index column in both row
res2 = arr[1,2]
print("\nelements present at 1st index row:\n", res)
print("\nelement present at 0th and 1st row both:\n", res1)
print("\nelement present at 1st index row and 2nd index column:\n", res2)

# print sum of array element using for loop :

sum = 0
# Loop through each row
for row in arr:
    # Loop for each element in the row
    for element in row:
      sum += element

print("\nSum of all elements in the array:\n", sum)

# other operations without using loop :
arr = np.array([[40,60,80],[50,70,10], [100,200,300], [24,34,56]])
print("\nsum of all elements of array:\n", arr.sum())                         # total sum
print("\nsum of all rows elements of array:\n", arr.sum(1))
print("\nmean of all rows elements of array:\n", arr.mean(1))
print("\nmean of all columns elements of array\n", arr.mean(0))

arr1 = np.array([[1,2,3], [5,6,7], [3,7,2]])
arr2 = np.array([[1,20,30], [50,6,70], [6,3,5]])
print("\narray 1:\n", arr1)
print("\narray 2:\n", arr2)

print("\naddition of two array\n", arr1+arr2)
print("\nsubtraction of two array\n", arr1-arr2)
print("\nmultiplication of two array\n", arr1*arr2)
print("\ndivision of two array\n", arr1/arr2)






