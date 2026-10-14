#local, global variable
# local, global variable
a = 1

def f1():
    b = 2
    print(a)
    print(b)
    #print(c)  # ERROR: c is not defined globally or locally in f1()

def f2():
    c = 2
    print(a)
    #print(b)  # ERROR: b is local to f1()
    print(c)

f1()
f2()
print(a)
#print(b)  # ERROR: b is a local variable inside f1()
#print(c)  # ERROR: c is a local variable inside f2()   

#call by value, call by reference
# call by value 
def f1(a):
    a = 100
a = 4
f1(a)
print(a)  # Output: 4
#call by reference
def f2(a):
    a = [10, 20, 30]  # Reassigns the local parameter
    a[2] = 200

a = [1, 2, 3]
f2(a)
print(a)  # Output: [1, 2, 3]  

#modifying list inside a function
def f3(a):
    a[2] = 200

a = [1, 2, 3]
f3(a)
print(a)  # Output: [1, 2, 200]
# recursive funcntions
def f1(n):
    if n == 0:          # Base condition
        return
    print("Hello")
    f1(n - 1)           # Recursive call

f1(3)
# factorial 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
# fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8