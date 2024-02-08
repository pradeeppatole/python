string = "Hello guys how are you doing, I am also doing good and I am learning python with the testing academy"

print(string[0:3])
print(string[6:10])
print(string[0:40:2])  # slicing with the steps

# Reverse slicing

print(string[40:0:-2])

print(string[40:0:-1])

print(string[40:0])

# partial slicing

print(string[:9])
print(string[9:])

print(string[:])
print(string[::-1])

# How to reverse the strings in python

string2 = "Hello"[::-1]
print(string2)