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
# a = set()#normal loop

# for x in range(1, 21):
#     if x % 2 == 0:
#         a.add(x)

# print(a)

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
def numbers():
    yield 1 
    yield 2 
    yield 3 
    yield 4 
n = numbers() 
print(n)
print(type(n))
print(next(n))
print(next(n))
print(n.__next__())
print(n.__next__())
print(next(n)) 

def evennumbers():
    for x in range(1, 10):
        if x % 2 == 0:
            yield x 
n = evennumbers()
print(next(n))
print(n.__next__())
for x in n:
    print(x)