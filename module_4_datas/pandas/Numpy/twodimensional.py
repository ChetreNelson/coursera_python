import numpy as np
x = [[1, 2, 3], [4, 5, 6]]
y = [[10, 20, 30],[40, 50, 60]]

a = np.array(x)
b = np.array(y)

# print(a)

# print(a.ndim)

# print(a.size)

# print(a.shape)


# acessing elements in the 2d 

# print(a[1,2])

# print(a[1][2])

print(a[0:2][1])
print(a[0:2,1])

# print(np.add(a,b))

# print(np.multiply(a,b))

# print(np.dot(a,b))

# print(a.T) #  transpose of the matrix