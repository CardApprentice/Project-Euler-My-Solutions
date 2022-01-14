# If we list all the natural numbers below 10 that are multiples of 3 or 5,
#  we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


import numpy as np
# First list all the numbers that are multiples of 3 below 1000
# then for 5, then delete duplicates
x = np.arange(3,1000,3).tolist()
y = np.arange(5,1000,5).tolist()

for i in y[:]:
    if i in x:
        y.remove(i)
print(y)

# sum up
x_sum = sum(x)
y_sum = sum(y)
output = x_sum + y_sum
print(output)