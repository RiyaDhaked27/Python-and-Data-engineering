# ****************************************** Assignment 8 ******************************************

import numpy as np
print(np.__version__)

# >>>>>>>>>>>>>>>>>>>>>>>> Question 1 >>>>>>>>>>>>>>>>>>>>>>>>>>
# create numpy array(1D, 2D, 3D)........ :
arr = np.array([45,36,23,89,90])
print("1D array is:\n",arr)
arr = np.array([[4,6,8],[5,7,1], [10,20,30]])
print("(3x3) 2D array is:\n",arr)
arr = np.array([[[3,5,4],[2,8,3],[5,6,7]], [[4,9,1],[7,8,3],[3,0,4]]])           # no. of elements in each set = height
print("(2x3x3) 3D array:\n", arr)                                                # no of outer sets(2) = no. of rows
print(arr.shape)                                                                 # no. of inner sets in each row(3) = no. of columns

# create arrays with random values......... :
arr_1d = np.random.rand(5)
print(" 1D array with random values: \n", arr_1d)
arr_2d = np.random.rand(3,4)
print(" 2D array with random values: \n", arr_2d)
arr_3d = np.random.rand(2, 2, 3)
print(" 3D array with random values: \n", arr_3d)

# empty numpy array.......... :
arr = np.empty((4,2))
print("4x2 empty numpy array: \n", arr)

# full numpy array :
arr = np.full((4,2), 10)
print("4x2 full numpy array and filled with 10: \n", arr)

# (3x5) zeros array.............. :
arr = np.zeros((3,5))
print(" (3x5) array filled with zeros:\n", arr)

# (4x3x2) ones array.............. :
arr = np.ones((4,3,2))
print("\n(4x3x2) array filled with ones: \n", arr)

# >>>>>>>>>>>>>>>>>>>>>>>> Question 2 >>>>>>>>>>>>>>>>>>>>>>>>>>
# (3x3) 2D array with range 2 to 10 values :
arr = np.arange(2,11).reshape(3,3)
print("(3x3) 2D array with values from 2 to 10:\n", arr)

# >>>>>>>>>>>>>>>>>>>>>>>> Question 3 >>>>>>>>>>>>>>>>>>>>>>>>>>
arr = np.zeros(10)
arr[5] = 11
print("\nNull vector with sixth value as 11:\n", arr)

# >>>>>>>>>>>>>>>>>>>>>>>> Question 4 >>>>>>>>>>>>>>>>>>>>>>>>>>
arr = np.array([45,36,23,89,90])
print("\nReversed array:\n", arr[::-1])                               # negative indexing

# >>>>>>>>>>>>>>>>>>>>>>>> Question 5 >>>>>>>>>>>>>>>>>>>>>>>>>>
arr = np.array([1, 2, 3])
print("\nConverted into float array:\n", arr.astype(float))

