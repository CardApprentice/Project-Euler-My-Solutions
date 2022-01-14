# Each new term in the Fibonacci sequence is generated by adding 
# the previous two terms. By starting with 1 and 2, 
# the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence 
# whose values do not exceed four million, find the sum of the even-valued terms.


# Generate a list of values until 4 million
i = [1,2]         # two-value-long frame
fib_list = [1]    # starting 
max_value = 4000000

while i[1] < max_value:
    fib_list.append(i[1])
    new_value = sum(i)
    i[0] = i[1]
    i[1] = new_value

# Remove odds
# Notice that you need to include [:], 
# this will generate a copy for index indication
for j in fib_list[:]:
    if j % 2 != 0:
        fib_list.remove(j)

output = sum(fib_list)
print(output)