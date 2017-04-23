import numpy as np

a = np.array([1, 2, 3])  # Create a rank 1 array
type(a)  # print(s "<type 'numpy.ndarray'>"
print(a.shape)  # print(s "(3,)"
print(a[0], a[1], a[2])  # print(s "1 2 3"
a[0] = 5  # Change an element of the array
print(a)  # print(s "[5, 2, 3]"

b = np.array([[1, 2, 3], [4, 5, 6]])  # Create a rank 2 array
print(b.shape)  # print(s "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])  # print(s "1 2 4"

# functions
a = np.zeros((2, 2))  # Create an array of all zeros
b = np.ones((1, 2))  # Create an array of all ones
c = np.full((2, 2), 7)  # Create a constant array
d = np.eye(2)  # Create a 2x2 identity matrix
e = np.random.random((2, 2))  # Create an array filled with random values

# indexing

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

b = a[:, 1:3]
print(a[0, 1])  # Prints "2"
b[0, 0] = 77  # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])  # Prints "77"

# index of arrays
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[[0, 1, 2], [0, 1, 0]])
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # equivalent to the prior

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])
