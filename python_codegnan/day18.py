#List Comprehension
#for
a = []
for x in range(1, 11):
    a.append(x)
print(a)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#create with list comprehension

#for-if
a = []
for x in range(1,11):
    if x % 2 == 0:
        a.append(x) 
print(a)#[2, 4, 6, 8, 10]
#create with list comprehension

#for-if-for-if 
a = []
for x in range(1,5):
    if x % 2 == 0:
        for y in range(1,4):
            if x + y == 5:
                a.append((x,y))
print(a)#[(2, 3), (4, 1)]
#create with list comprehension
a = [
    (x, y)
    for x in range(1, 5)
    if x % 2 == 0
    for y in range(1, 4)
    if x + y == 5
]

print(a)#[(2, 3), (4, 1)]
#set comprehension: create a set with even numbers from 1 to 20
a = set()#normal loop

for x in range(1, 21):
    if x % 2 == 0:
        a.add(x)

print(a)

#Using set comprehension:
a = {x for x in range(1, 21) if x % 2 == 0}
print(a)#{2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
#dict comprehension: create a dict with numbers and their squares from 1 to 10 
a = {x: x**2 for x in range(1, 11)}#{key: value for variable in iterable}
print(a)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
#function
def numbers():
    return 1 #When Python encounters return, it immediately exits the function and sends the result back to the caller.
    return 2 
n = numbers()
print(n)# 1
print(type(n))# <class 'int'>

#generators
# Define a generator function named numbers
def numbers():
    yield 1  # Produce 1 and pause the generator
    yield 2  # Resume and produce 2
    yield 3  # Resume and produce 3
    yield 4  # Resume and produce 4

n = numbers()  # Create a generator object

print(n)  # Print the generator object's information
print(type(n))  # Print its type: <class 'generator'>

print(next(n))  # Get the first value: 1
print(next(n))  # Get the second value: 2
print(n.__next__())  # Get the third value: 3
print(n.__next__())  # Get the fourth value: 4

# No values remain, so this call raises StopIteration
# print(next(n))

# Define a generator function named evennumbers()
def evennumbers():
    # Generate numbers from 1 to 9
    for x in range(1, 10):
        # Check whether x is an even number
        if x % 2 == 0:
            # Produce the even number and pause the generator
            yield x
# Call the generator function and store the generator object in n
n = evennumbers()
# Get the first even number and print it: 2
print(next(n))
# Resume the generator, get the next even number, and print it: 4
print(n.__next__())
# Continue getting the remaining values from the generator
for x in n:
    # Print each remaining even number
    print(x)