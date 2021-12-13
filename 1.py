import numpy as np

Numbers = np.loadtxt("1.txt")

# Part 1 increase of next number
i = 0  # Loop counter
a = 0  # First number
b = 1  # Second number
c = 0  # Counter designates number of increases
while i < (len(Numbers) - 1):
    if Numbers[b] > Numbers[a]:
        c = c + 1
    b = b + 1
    a = a + 1
    i = i + 1


# Part 2 rolling average
i = 0
c = 2
increase = 0
list1 = [Numbers[0], Numbers[1], Numbers[2]]  # List with initial 3 numbers
while i < (len(Numbers) - 3):
    sum1 = sum(list1)         # Adds three numbers in list
    list1.pop(0)              # Removes first element in list
    c = c + 1                 # Increase counter for last number of the three
    list1.append(Numbers[c])  # Adds new number to list
    sum2 = sum(list1)         # New sum of three numbers
    if sum1 < sum2:
        increase = increase + 1
    i = i + 1

