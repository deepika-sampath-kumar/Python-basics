# Import python packages - NumPy (Numerical Python) and matplotlib 
import numpy as np 
import matplotlib.pyplot as plt 


# Create an 1D array 
lst = [1,2,3,4,5]
arr1 = np.array(lst)

# Print details
print(f'The array : {arr1}')
print(f'The shape of the array : {arr1.shape}')
print(f'The dimension of the array : {arr1.ndim}')
print(f'The data type in the array : {arr1.dtype}')

# Create a 2D array 
lst = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = np.array(lst,dtype = 'float')

# Print details
print(f'The array : {arr2}')
print(f'The shape of the array : {arr2.shape}')
print(f'The dimension of the array : {arr2.ndim}')
print(f'The data type in the array : {arr2.dtype}')

# Arange 
arange_array = np.arange(1,10,1) # same as range, array range
print(f' Arange array = {arange_array}')

# Reshape 
reshaped_array = arange_array.reshape(3,3)
print(f'The reshaped array = {reshaped_array}')

# Change the data type of the elements of the array 
print(f'The data type of the array = {reshaped_array.dtype}')
changed_dt_array = reshaped_array.astype(np.float32)
print(f'The changed data type = {changed_dt_array.dtype}')

# Linspace
lin_array = np.linspace(1,5,10)
print(f'The linspace array 1 to 5 into 10 : {lin_array}')

# Zeros 
zeros_array = np.zeros((3,3))
print(f'Zeros (3x3) = {zeros_array}')

# Ones
ones_array = np.ones((2,2))
print(f'Ones (2x2) = {ones_array}')

# Identity matrix 
eye_mat = np.eye((5))
print(f' Identity matrix (5,5) = {eye_mat}')

# Random number between 0 (included) and 1(excluded) 
rnd_01_1d = np.random.rand(10)
rnd_01_2d = np.random.rand(3,4)
print(f'The random number btw [0,1) 1D (10) = {rnd_01_1d}')
print(f'The random number btw [0,1] 2D (3X2) ={rnd_01_2d}')

# Random integer must define limits
np.random.seed(1)  # Have a defined randomness (inbuilt)
rnd_int_1d = np.random.randint(low=1 , high=6, size = 5) 
rnd_int_2d = np.random.randint(low = 10, high = 20, size = (2,2))
print(f'The random number btw [0,1) 1D (5) = {rnd_int_1d}')
print(f'The random number btw [0,1] 2D (2X2) = {rnd_int_2d}')

# Plot a quadratic function 
x_data = np.linspace(0,10,100)
y_data = x_data**2
plt.figure(figsize= (7,7))
plt.grid()
plt.title('Quadratic function - Line plot',color='maroon',fontsize= 18)
plt.xlabel('X [units]',color = 'g',fontsize= 12)
plt.ylabel('Y= X^2 [units]',color='g',fontsize=12)
plt.plot(x_data,y_data) # Line plot 
plt.show()

plt.figure(figsize = (7,7))
plt.grid()
plt.title('Quadratic function - Scatter plot',color='maroon',fontsize= 18)
plt.xlabel('X [units]',color = 'g',fontsize= 12)
plt.ylabel('Y= X^2 [units]',color='g',fontsize=12)
plt.scatter(x_data, y_data) # Scatter plot 
plt.show()