# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# define a function that detects palindromic numbers
def palind_num(x):
    # first find the length of this number
    original_number = str(x)
    l = len(original_number)
    reverse_number = ""
    # pick the digits out and remake this number
    for i in range(l):
        reverse_number += original_number[l-1-i]
    y = int(reverse_number)

    if x == y:
        return True
    else:
        return False


# now look for all numbers that are products of two 3-digit numbers
product_of_2_3digit = [x*y for x in range(100, 999) for y in range(100, 999)]
product_of_2_3digit = sorted(set(product_of_2_3digit), reverse=True)

# test them from largest to smallest
for i in product_of_2_3digit:
    if palind_num(i):
        print(i)
        break
