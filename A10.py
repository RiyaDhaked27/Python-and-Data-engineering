# ****************************************** Assignment 10 *****************************************

import numpy as np
# import matplotlib.pyplot as plt

# >>>>>>>>>>>>>>>>>>>>>>>> Question 1 >>>>>>>>>>>>>>>>>>>>>>>>>>

arr2d = np.array([[1,2,3], [np.nan,5,6], [7,np.nan,9], [10,11,np.nan]])
print("\n2D Array is with nan:\n", arr2d)

# replace nan with zero :
res = np.nan_to_num(arr2d, copy=False, nan=0)
print("\nAfter replacing nan with zero array is:\n", res)

# Interchange 3 rows and 3 columns :
arr2d[:,[0,1,2]] = arr2d[:,[1,2,0]]
print("\nafter interchange 3 columns array is\n", arr2d)

arr2d[[0,1,2],:] = arr2d[[1,2,0],:]
print("\nafter interchange 3 rows array is\n", arr2d)

# >>>>>>>>>>>>>>>>>>>>>>>> Question 2 >>>>>>>>>>>>>>>>>>>>>>>>>>

#move axes of 3D numpy array to new position(transpose)
arr = np.array([[[3,5,4],[2,8,3]], [[4,9,1],[7,8,3]]])
print("\n3D array:\n", arr)

res = arr.transpose(2,0,1)
print("\nAfter transpose:\n", res)

# >>>>>>>>>>>>>>>>>>>>>>>> Question 3 >>>>>>>>>>>>>>>>>>>>>>>>>>
# replace nan values with average of columns
arr2d = np.array([[1,2,3], [np.nan,5,6], [7,np.nan,9], [10,11,np.nan]])
print("\n2D Array is with nan:\n", arr2d)

col_mean = np.nanmean(arr2d, axis=0)
print("\nmean of 2D Array:\n", col_mean)

pos = np.isnan(arr2d)
print("\npositions of nan in this 2D Array are:\n", pos)

arr2d[pos] = col_mean
print("\nAfter nan replace with mean of columns:\n", arr2d)

# >>>>>>>>>>>>>>>>>>>>>>>> Question 4 >>>>>>>>>>>>>>>>>>>>>>>>>>
# replace the negative value with zero :

arr = np.array([[1,2,-3],[4,-5,-6],[5,6,7],[-11,10,21]])
print("\n2D Array is with nan:\n", arr)

res = np.where(arr<0, 0, arr)
print("\nAfter replace the negative value with zero\n", res)

# >>>>>>>>>>>>>>>>>>>>>>>> Question 5,6 >>>>>>>>>>>>>>>>>>>>>>>>>>

arr1 = np.array([3, 4, 5, 6, 7])
arr2 = np.array([1, 0, 8, 6, 9])
print("\nArray 1:\n", arr1)
print("\nArray 2:\n", arr2)

# Calculate the average of the two arrays
avg = (arr1 + arr2) / 2
print("\nAverage of NumPy arrays:\n", avg)

# >>>>>>>>>>>>>>>>>>>>>>>> Question 7 >>>>>>>>>>>>>>>>>>>>>>>>>>
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("\n2D Array 1:\n", a)
print("\n2D Array 2:\n", b)

# Combine both arrays
combined = np.concatenate((a, b), axis=0)

# Calculations
average = np.mean(combined)
mean = np.mean(combined)
median = np.median(combined)
#mode = stats.mode(combined, axis=None)

print("Combined array:\n", combined)
print("Average:", average)
print("Mean:", mean)
print("Median:", median)
#print("Mode:", mode.mode[0])


# >>>>>>>>>>>>>>>>>>>>>>>> Question 8 >>>>>>>>>>>>>>>>>>>>>>>>>>
A = np.array([
    [1, -2, 3],
    [-1, 3, -1],
    [2, -5, 5]
])
B = np.array([9, -6, 17])

res = np.linalg.solve(A, B)
print("Solution [x, y, z]:", res)

# inverse matrix method :
res_inv = np.linalg.inv(A)
print("\ninverse matrix method:\n", res_inv)


# >>>>>>>>>>>>>>>>>>>>>>>> Question 9 >>>>>>>>>>>>>>>>>>>>>>>>>>

import matplotlib.pyplot as plt

# subjects and marks :
subjects = ['Math', 'Physics', 'Chemistry', 'Communication']
sem1 = [85, 78, 90, 88]
sem2 = [82, 80, 92, 85]

x = np.arange(len(subjects))


plt.figure(figsize=(8,5))
plt.bar(x - 0.2, sem1, width=0.4, label='Semester 1', color='blue')
plt.bar(x + 0.2, sem2, width=0.4, label='Semester 2', color='orange')

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Semester 1 vs Semester 2 Marks Comparison")
plt.legend()                                 # legend() = which color show sem 1 or sem 2
plt.grid(True)
plt.show()




