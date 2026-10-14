def add(a, b):
    print('add function')
    c = a + b
    return c
    pirnt('HI')  # ERROR: Typo in print; also unreachable after return


def sub(a, b):
    print('sub function')
    c = a - b
    return  # ERROR: Returns None; use return c


def div(a, b):
    print('div function')
    c = a / b
    # ERROR: Missing return c


x = add(10, 15)
y = sub(20, 10)
z = div(25, 10)

print(x)
print(y)
print(z)
print()


# Type of arguments
def detail(name, age, rollno):
    print(f'My name is {name}')
    print(f'My age is {age}')
    print(f'My rollno is {rollno}')


detail('rakesh', 20, 'A101')
detail(20, 'A101', 'rakesh')  # No error, but arguments are in the wrong order
detail(age=20, rollno='A101', name='rakesh')
detail(rollno='A101', age=20, name='rakesh')


def add(a, b=10, c=20):
    return a + b + c

print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(c=3, a=1, b=2))


# Order of = in function definition
# def sub(a=10, b, c):  # ERROR: Non-default argument follows default argument
#     pass

# Correct:
def sub(a, b, c=10):
    pass


# Order of = in function call
# add(a=10, b, c)  # ERROR: Positional arguments cannot follow keyword arguments

# Correct:
add(10, b=20, c=30)


def f1(*a):
    print(a)
    print(type(a))

f1(1, 2, 3, 4)


def f2(**a):
    print(a)
    print(type(a))

# f2(1, 2, 3, 4)  # ERROR: **kwargs does not accept positional arguments
f2(a=1, b=2, c=3, d=4)  # Correct