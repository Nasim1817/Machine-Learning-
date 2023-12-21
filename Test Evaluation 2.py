#!/usr/bin/env python
# coding: utf-8

# ### Questions 1
# 
# Create a matrix of 5x5 with random integers, after that swap its first and last rows.

# In[13]:


import numpy as np


# In[11]:


matrix = np.random.randint(1, 100, size=(5, 5))
print("Random integers Matrix :")
print(matrix)
matrix[0, :], matrix[-1, :] = matrix[-1, :], matrix[0, :]
print("swapping first and last rows:")
print(matrix)


# ### Question 2
# 
# Create a 2D array, remove all rows that contain at least one zero.

# In[56]:


array = np.array([[1, 2, 3], [0, 0, 0], [4, 5, 6],
                 [0, 0, 0], [7, 8, 9], [0, 0, 0]])
print("Original Dataset")
print(array)
array = array[~np.all(array == 0, axis=1)]
print("After removing rows")
print(array)


# ### Question 3
# 
# Write a NumPy program to find the real and imaginary parts of an array of complex numbers.<br>
# Original array [ 1.00000000+0.j 0.70710678+0.70710678j]

# In[50]:


x = np.sqrt([1 + 0j])
y = np.sqrt([0 + 1j])

print("Original array:x ", x)
print("Original array:y ", y)
print("Real part of the array:")
print(x.real)
print(y.real)
print("Imaginary part of the array:")
print(x.imag)
print(y.imag) 


# ### Question 4
# 
# Write a NumPy program to remove the duplicate elements of an array.<br>
# Original array:
# [10 10 20 20 30 30]
# 

# In[32]:


original_array = np.array([10, 10, 20, 20, 30, 30])
unique_array = np.unique(original_array)
print("Original array:")
print(original_array)
print("removing duplicates:")
print(unique_array)


# ### Question 5
# 
# Write a NumPy program to create a 3x3x3 array with random values.

# In[33]:


random_array = np.random.rand(3, 3, 3)
print("3x3x3 Array with Random Values:")
print(random_array)


# ### Question 6
# 
# Write a NumPy program to create a random vector of size 10 and sort it.
# <b>Note:<\b> Do not use builtin sorting function

# In[34]:


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

random_vector = np.random.rand(10)

print("Original vector:")
print(random_vector)
bubble_sort(random_vector)
print("Sorted vector:")
print(random_vector)


# ### Question 7
# 
# Write a NumPy program to check two random arrays are equal or not.

# In[36]:


array1 = np.random.rand(5)
array2 = np.random.rand(5)
print("Array 1:")
print(array1)
print("Array 2:")
print(array2)
are_equal = np.array_equal(array1, array2)
if are_equal:
    print("both array are equal.")
else:
    print("both array are not equal.")


# ### Question 8 
# 
# Write a NumPy program to sort a given array of shape 2 along the first axis, last axis and on flattened array.<br>
# 
# Original array:<br>
# [[10 40]<br>
# [30 20]]

# In[31]:


original_array = np.array([[10, 40],
                           [30, 20]])
sorted_first_axis = np.sort(original_array, axis=0)
sorted_last_axis = np.sort(original_array, axis=-1)
sorted_flattened = np.sort(original_array.flatten())

print("Original array:")
print(original_array)
print("Sorted the first axis:")
print(sorted_first_axis)
print("Sorted the last axis:")
print(sorted_last_axis)
print("Sorted flattened array:")
print(sorted_flattened.reshape(original_array.shape))


# ### Question 9
# 
# Write a NumPy program to get the floor, ceiling and truncated values of the elements of a numpy array.<br>
# 
# Original array:<br>
# [-1.6 -1.5 -0.3 0.1 1.4 1.8 2. ]

# In[45]:


x = np.array([-1.6, -1.5, -0.3, 0.1, 1.4, 1.8, 2.0])
print("Original array:")
print(x)

print("Floor values of the array elements:")
print(np.floor(x))

print("Ceil values of the array elements:")
print(np.ceil(x))

print("Truncated values of the above array elements:")
print(np.trunc(x)) 


# ### Questions 10
# 
# Write a NumPy program to display all the dates for the month of March, 2017

# In[47]:


print("March, 2017")
print(np.arange('2017-03', '2017-04', dtype='datetime64[D]'))


# ### Question 11
# 
# Write a NumPy program to create 24 python datetime.datetime objects (single object for every hour), and then put it in a numpy array.

# In[49]:


import datetime
start = datetime.datetime(2000, 1, 1)
datetime_array = np.array([start + datetime.timedelta(hours=i) for i in range(24)])
print(datetime_array) 


# ### Question 12
# 
# Write a NumPy program to concatenate element-wise two arrays of string.<br>
# <b>Example <\b>
# Array1:<br>
# ['Python' 'PHP']<br>
# Array2:<br>
# [' Java' ' C++']<br>
# new array:<br>
# ['Python Java' 'PHP C++']<br>

# In[40]:


array1 = np.array(['Python', 'PHP'])
array2 = np.array([' Java', ' C++'])
concatenate_array = np.core.defchararray.add(array1, array2)
print("Array1:")
print(array1)
print("Array2:")
print(array2)
print("Concatenate array:")
print(concatenate_array)

