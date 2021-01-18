# Lists in python
x = [10, 20, 30, 40, 50, 60]
print(x)
print(x[2])

# tuples in python..this is similar to lists in python
y = (1, 2, 3, 4, 5, 5)
print(y)
print(y[0])

# count the number of 5s in the tuple
print("num of 5s : " + str(y.count(5)))

# get the length of the tuple
print("Length of the tuple is " + str(len(y)))

# Concate 2 tuples
a = (4, "max", 4, 8)
b = y + a
print(b)

# print maximum value
print("Max value of y is: " + str(max(y)))

c = ("hello", ) * 5
print(c)