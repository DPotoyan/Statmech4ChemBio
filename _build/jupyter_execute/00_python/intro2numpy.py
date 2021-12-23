#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#NumPy" data-toc-modified-id="NumPy-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>NumPy</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Numpy-Arrays:-overview" data-toc-modified-id="Numpy-Arrays:-overview-1.0.1"><span class="toc-item-num">1.0.1&nbsp;&nbsp;</span>Numpy Arrays: overview</a></span></li></ul></li><li><span><a href="#Array-Creation" data-toc-modified-id="Array-Creation-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Array Creation</a></span><ul class="toc-item"><li><span><a href="#Generating-numpy-arrays-from-lists" data-toc-modified-id="Generating-numpy-arrays-from-lists-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Generating numpy arrays from lists</a></span></li><li><span><a href="#Array-vs-list-cration:-which-is-faster?" data-toc-modified-id="Array-vs-list-cration:-which-is-faster?-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Array vs list cration: which is faster?</a></span></li><li><span><a href="#Generating-arrays-using-special-methods" data-toc-modified-id="Generating-arrays-using-special-methods-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Generating arrays using special methods</a></span></li><li><span><a href="#Summary-of-common-array-creation-methods" data-toc-modified-id="Summary-of-common-array-creation-methods-1.1.4"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Summary of common array creation methods</a></span></li></ul></li><li><span><a href="#Indexing,-slicing-and-shaping-arrays" data-toc-modified-id="Indexing,-slicing-and-shaping-arrays-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Indexing, slicing and shaping arrays</a></span><ul class="toc-item"><li><span><a href="#Vectorized-operations-with-numpy" data-toc-modified-id="Vectorized-operations-with-numpy-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Vectorized operations with numpy</a></span></li><li><span><a href="#Aggregation" data-toc-modified-id="Aggregation-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Aggregation</a></span></li><li><span><a href="#Reshaping-arrays" data-toc-modified-id="Reshaping-arrays-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Reshaping arrays</a></span></li><li><span><a href="#Broadcasting-rules-of-numpy-arrays" data-toc-modified-id="Broadcasting-rules-of-numpy-arrays-1.2.4"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>Broadcasting rules of numpy arrays</a></span></li><li><span><a href="#Pandas" data-toc-modified-id="Pandas-1.2.5"><span class="toc-item-num">1.2.5&nbsp;&nbsp;</span>Pandas</a></span></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-1.2.6"><span class="toc-item-num">1.2.6&nbsp;&nbsp;</span>Exercises</a></span></li></ul></li></ul></li></ul></div>

# # NumPy

# NumPy is the core library for numerical and scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays. 

# To use NumPy, we first need to import the `numpy` package:

# In[1]:


import numpy as np
print(np.__version__)


# ### Numpy Arrays: overview

# - A numpy array is a grid of values, all of the same type, and is indexed by nonnegative integers. 
# - The array can have any number of dimensions 1D, 2D, 3D, ...
# - The shape of an array is a tuple of integers giving the size of the array along each dimension. For example a 1D vector of size 4 is (4,). a matrix of size 2 is (2,2), a matrix with size 2x5 is (2,5) 
# 
# - Numpy arrays can be generates either by feeding lists to numpy or on the fly using numpy special methods

# ## Array Creation

# ### Generating numpy arrays from lists

# In[2]:


data=np.array([1,2,3])
data


# In[3]:


data.shape


# ![](./figs/numpy1.png)

# In[4]:


print(data[0], data[1], data[2]) 
data[0] = 10                 # Change an element of the array
print(data)                   


# In[5]:


b = np.array([[1,2,3],[4,5,6]])   # Create a 2D array
print(b)


# In[6]:


print(b.shape)                    
print(b[0, 0], b[0, 1], b[1, 0])


# In[7]:


# Question: what does this do?
np.array( [ xx**2 for x in range(100) if x%3==0 ])


# ### Array vs list cration: which is faster?
# 
# Jupyter notebooks have a nice built-in method to time how long a line of code takes to execute. In a Jupyter notebook, when a line starts with ```%timeit``` followed by code, the kernel runs the line of code multiple times and outputs an average of the time spent to execute the line of code.
# 
# We can use ```%timit``` to compare a mathematical operation on a Python list using a for loop to the same mathematical operation on a NumPy array.

# In[ ]:


lst = list(range(10000))
get_ipython().run_line_magic('timeit', 'for i, item in enumerate(lst): lst[i] = lst[i]*2')


# In[ ]:


nparray = np.arange(0,10000,1)
get_ipython().run_line_magic('timeit', '2*nparray')


# With 10,000 integers, the Python list and for loop takes an average of single milliseconds, while the NumPy array completes the same operation in tens of microseconds. This is a speed increase of over 100x by using the NumPy array (1 millisecond = 1000 microseconds).
# 
# For larger lists of numbers, the speed increase using NumPy is considerable.

# ### Generating arrays using special methods

# ![](./figs/numpy2.png)

# In[ ]:


a = np.zeros((5,8))  # Create an array of all zeros
print(a)


# In[ ]:


b = np.ones((1,5))   # Create an array of all ones
print(b) 


# In[ ]:


e = np.random.random((4,4)) # Create an array filled with random values
print(e)


# In[ ]:


x = np.linspace(1,100,10) # create an array between 1 and 100 divided by 10 segments
print(x)


# In[ ]:


y = np.arange(1,100,5) # create an array strting from 1 to 100 in 10 incremenets
print(y)


# In[ ]:


c = np.full((2,2), 7.5) # Create a constant array
print(c)  


# In[ ]:


d = np.eye(5)        # Create a 3x3 identity matrix
print(d) 


# In[ ]:


k = np.tile(d,3)  # repeat the array d 3 times
k


# ### Summary of common array creation methods
# 
# Below is a list of NumPy functions and associated descriptions used in this section.
# 
# | Function | Description |
# | --- | --- |
# | ```np.array([list, of, numbers])``` | Array from a list |
# | ```np.arange(start, stop, step)``` | Array with know step |
# | ```np.linspace(start, stop, num)``` | Array with known num |
# | ```np.logspace(start, stop, num)``` | Logorithmically spaced array |
# |```np.zeros((rows, cols))``` | Array of zeros |
# | ```np.ones((rows, cols))``` | Array of ones |
# | ```np.random.randint(start, stop, num)``` | Random integers |
# | ```np.random.rand(num)``` | Random float 0 to 1 |
# | ```np.random.choice(list, num)``` | Randome choice from a list | 
# | ```np.random.randn(num)``` | Random normal distribution |
# | ```np.meshgrid(array1, array2)``` | Two 2D arrays from two 1D arrays  |
# | ```np.mgrid[start:stop:step, start:stop:step]``` | MATLAB meshgrid |

# ## Indexing, slicing and shaping arrays

# **Slicing:** Similar to Python lists, numpy arrays can be sliced. Since arrays may be multidimensional, you must specify a slice for each dimension of the array:

# In[ ]:


data=np.array([1,2,3])
data[0:3]


# ![](./figs/numpy_index.png)

# In[ ]:


data = np.array([[1,3,5], [2,4,6]])
data.T


# ![](./figs/numpy-matrix-indexing.png)

# In[ ]:


a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
a.shape


# In[ ]:


a.shape


# In[ ]:


a[1,:4]  #


# In[ ]:


a[1,3]


# In[ ]:


a[:,-1] # last column


# In[ ]:


a[-1,:] # last row


# **Same principles of slicing and shapes applies to the N-dimensional arrays.**

# ![](./figs/numpy_3d.png)

# ### Vectorized operations with numpy

# Basic mathematical functions operate **elementwise on arrays**, and are available both as operator overloads and as functions in the numpy module:

# In[ ]:


x = np.array([1,2,3,4])
y = np.array([5,6,7,8])


# In[ ]:


# Elementwise sum; both produce the array
print(x + y) 


# In[ ]:


# Elementwise difference; both produce the array
print(x - y)  


# In[ ]:


# Elementwise product; both produce the array
print(x * y) 


# In[ ]:


print(x / y) 


# In[ ]:


print(np.sqrt(x)) 


# In[ ]:


1.5*x  # elementwise multiplication!


# In[ ]:


y+3    # elementwise addition. 


# As last two examples show can also do operations on arrays with unequal shapes! These are powerful operations which follow set of rules called **broadcasting.** See the end for these rules and examples

# **To use vector,matrix dot product between A and B use A@B**

# In[ ]:


x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v@w) 


# In[ ]:


# Matrix / vector product; both produce the rank 1 array [29 67]
print(x@v) 


# In[ ]:


# Matrix / matrix product; both produce the rank 2 array
print(x@y) 


# ### Aggregation

# Numpy provides many useful functions for performing computations on arrays; one of the most useful is `sum`:

# In[ ]:


x = np.array([[1,2],[3,4]])
np.sum(x,axis=1)


# In[ ]:


print(np.sum(x))   # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))   # Compute sum of each row; prints "[3 7]"


# In[ ]:


print(x.max())
print(x.min())


# ### Reshaping arrays

# In[ ]:


x=np.array([1,2,3,4,5,6,7,8,9,10])


# In[ ]:


x=x.reshape(2,5)
x


# In[ ]:


x=x.reshape(5,2)
x


# In[ ]:


x.T # transpose matrix


# ### Broadcasting rules of numpy arrays

# Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations. Frequently we have a smaller array and a larger array, and we want to use the smaller array multiple times to perform some operation on the larger array. 

# The rules of broadcasting are:
# 
# - **Rule 1:** If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones on its leading (left) side.
# - **Rule 2:** If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
# - **Rule 3:** If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

# ![](./figs/numpy-matrix-broadcast.png)

# **Examples of broadcasting**

# In[ ]:


data     = np.array([[1,2],[3,4],[5,6]])
ones_row = np.array([1,1])
data.shape, ones_row.shape


# In[ ]:


data


# In[ ]:


ones_row


# In[ ]:


data.shape, ones_row.shape


# In[ ]:


data+ones_row


# **Let us see both rules in action on another example**

# In[ ]:


a = np.arange(3).reshape((3, 1))
print(a)
print(a.shape)


# In[ ]:


b = np.arange(3)
print(b)
print(b.shape)


# Lets predict a+b sum. By first rule the sum of arrays with shapes **(3,1)+(3,)** are broadcast to **(3,1)+(1,3)** then by second rule dimensions one are padded to match the shape **(3,3)+(3,3)**

# In[ ]:


a+b 


# ### Pandas

# You may thinkg of numpy as enhancing functionality of lists for numerical computations. In the same vein you can think of pandas as enahcnign dicitonaires to deal with heteogenuous categorical data. 
# 
# Pandas is widely used by data analysts from all disciplines to carry out rapid data cleaning, statistical analysis and plotting. The DataFrame is the ore object of pandas whihc stores observables as columns whith rows indicating measurments or samples. Lets create an example

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


A = pd.DataFrame({'Time': [1,2,3,4,5],
                 'Energy': [10,20,30,40,50]
                 })


# In[ ]:


A


# In[ ]:


A['velocity'] = np.zeros(5)


# In[ ]:


A.columns


# In[ ]:


A.index


# In[ ]:


# acess underlying values as numpy arrays
A['Energy'].values


# ### Exercises

# ```{admonition} Exercise-1,  Array Creation
# **Predict and explain the following statements**
# 
# 1. Create an array of the numbers ```1```, ```5```, ```19```, ```30```
# 
# 2. Create an array of the numbers ```-3```, ```15```,```0.001```, ```6.02e23```
# 
# 3. Create an array of integers between -10 and 10
# 
# 4. Create an array of 10 equally spaced angles between 0 and 2$\pi$
# 
# 5. Create an array of logarithmically spaced numbers between 1 and 1 million. Hint: remember to pass exponents to the ```np.logspace()``` function.
# 
# 6. Create an array of 20 random integers between 1 and 10
# 
# 7. Create an array of 30 random numbers with a normal distribution
# ```

# ```{admonition} Exercise-2,  Array Manipulation
# 
# **Create an array ```B``` that contains integers 0 to 24 (including 24) in one row.  Then reshape ```B``` into a 5 row by 5 column array**
# 
# Extract the 2nd row from ```B```.  Store it as a one column array called ```x```.
# 
# Store the number of elements in array ```x``` in a new variable called ```y```. 
# 
# Extract the last column of ```B``` and store it in an array called ```z```.  
# 
# Store a transposed version of ```B``` in an array called ```t```.

# ```{admonition} Exercise-3,  Array Manipulation
# 
# 
# **The 1D NumPy array ```B``` is defined below.  But your code should work with any 1D NumPy array filled with numeric values. **
# 
# ```G = np.array([5, -4.7, 99, 50, 6, -1, 0, 50, -78, 27, 10])```
# 
# (a) Select all of the positive numbers in ```G``` and store them in ```x```.
# 
# (b) Select all the numbers in ```G``` between ```0``` and  ```30``` and store them in ```y```.
# 
# (c) Select all of the numbers in ```G``` that are either less than ```-50``` or greater than ```50``` and store them in ```z```.
# 
# ```

# ```{admonition} Exercise-4: Basic numpy operations
# 
# 1. Import the numpy package under the name `np` 
# `hint: import … as`
# 
# 2. Print the numpy version and the configuration 
# `hint: np.__version__, np.show_config)`
# 
# 3. Create a null vector of size 10 
# `hint: np.zeros`
# 
# 4. How to find the memory size of any array 
# `hint: size, itemsize`
# 
# 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
# `hint: np.info`
# 
# 6. Create a null vector of size 10 but the fifth value which is 1 
# `hint: array[4]`
# 
# 7. Create a vector with values ranging from 10 to 49 
# `hint: arange`
# 
# 8. Reverse a vector (first element becomes last) 
# `hint: array[::-1]`
# 
# 9. Create a 3x3 matrix with values ranging from 0 to 8 
# `hint: reshape`
# 
# 10. Find indices of non-zero elements from [1,2,0,0,4,0] 
# `hint: np.nonzero`
# 
# 11. Create a 3x3 identity matrix 
# `hint: np.eye`
# 
# 12. Create a 3x3x3 array with random values 
# `hint: np.random.random`
# 
# 13. Create a 10x10 array with random values and find the minimum and maximum values 
# `hint: min, max`
# 
# 14. Create a random vector of size 30 and find the mean value 
# `hint: mean`
# 
# 15. Create a 2d array with 1 on the border and 0 inside 
# `hint: array[1:-1, 1:-1]`
# 
# 16. How to add a border (filled with 0's) around an existing array? 
# `hint: np.pad`
# 
# 17. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal 
# `hint: np.diag`
# 
# 18. Create a 8x8 matrix and fill it with a checkerboard pattern 
# `hint: array[::2]`
# 
# 19. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
# `hint: np.unravel_index`
# 
# 20. Create a checkerboard 8x8 matrix using the tile function 
# `hint: np.tile`
# 
# 21. Normalize a 5x5 random matrix 
# `hint: (x -mean)/std`
# 
# 22. Create a custom dtype that describes a color as four unsigned bytes (RGBA) 
# `hint: np.dtype`
# 
# 23. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) 
# `hint:`
# 
# 24. Given a 1D array, negate all elements which are between 3 and 8, in place. 
# `hint: >, <`
# 
# 25. What is the output of the following script? 
#     ```python
#     # Author: Jake VanderPlas
# 
#     print(sum(range(5),-1))
#     from numpy import *
#     print(sum(range(5),-1))
#     ```
# `hint: np.sum`
# 
# 26. Consider an integer vector Z, which of these expressions are legal? 
#     ```python
#     Z**Z
#     2 << Z >> 2
#     Z <- Z
#     1j*Z
#     Z/1/1
#         Z<Z>Z
#     ```
# 27. What are the result of the following expressions?
#     ```python
#     np.array(0) / np.array(0)
#     np.array(0) // np.array(0)
#     np.array([np.nan]).astype(int).astype(float)
#     ```
# 
# 28. How to round away from zero a float array ? 
# `hint: np.uniform, np.copysign, np.ceil, np.abs, np.where`
# 
# 29. How to find common values between two arrays? 
# `hint: np.intersect1d` 
# 
# 30. Create random vector of size 10 and replace the maximum value by 0
# ```

# In[ ]:




