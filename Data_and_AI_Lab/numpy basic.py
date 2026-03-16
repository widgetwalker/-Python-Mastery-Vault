import numpy as np

n = 10
arr = np.zeros(n)

# Take 10 numbers as input from user
print("Enter 10 numbers:")
for i in range(n):
    arr[i] = float(input()) 

# Calculate total, average, max, min
total = np.sum(arr)
average = np.average(arr)
maxim = np.max(arr)  
minim = np.min(arr)

# Print the results 
print("Total =", total)
print("Average =", average)
print("Maximum Value =", maxim)  
print("Minimum Value =", minim)