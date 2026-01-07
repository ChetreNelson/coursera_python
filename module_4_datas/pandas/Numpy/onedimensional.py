import numpy as np 
import matplotlib.pyplot as plt
a = np.array([1,2,3,4])
# print(a)

#checking type
# print(type(a))

#size
# print(a.size)

# checking dimension
# print(a.ndim) 

# checking data type
# print(a.dtype)

# slicling
# print(a[1:3])
# print(a[1:4:2]) # using steps 

# can acess using list
select = [0, 2]
# print(a[select])

# print(a.mean())
# print(a.std()) #standard deviation

#using max() and min() to find min max

#using add() , subtract() , multiply(), divide() , dot() function 

# adding constant to 1 to each element like adding constants
# print (a + 1)

# mathematical functions
# print(np.pi)
# print(np.sin(a))

# linspace
arr = np.linspace(-2, 2, num=5)
# print(arr)

x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)
# plt.plot(x, y)

# can print as list as well
# for x in arr:
#     print(x)

# various mathematical operation
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))