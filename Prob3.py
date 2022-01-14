# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


import numpy as np
import math
# The factor ranges from 2 to sqrt of the number.
target_num = 600851475143
candidate_list = np.arange(2,math.floor(np.sqrt(target_num))).tolist()
max_prime_factor = 1 # initialization, i know 1 is not prime
non_prime_flag = 0

# test every candidate if they are factors
for i in candidate_list:
    if target_num % i == 0:
        # next we test if they are prime
        for j in np.arange(2,i-1).tolist():
            if i % j == 0:
                non_prime_flag = 1
                break
        # you are prime
        if non_prime_flag != 1:
            max_prime_factor = np.max([i, max_prime_factor])

print(max_prime_factor)
