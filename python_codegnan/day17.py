#Normal function vs lambda function
def add(x, y):         
    return x + y 
print(add(10,20))      #30 
print(type(add))       #<class 'function'>

a = lambda x,y : x + y   
print(a(10,20))        #30
print(type(a))        #<class 'function'>

#b = lambda (x,y) : x + y   You cannot put separate parameters inside parentheses like (x, y) in a lambda definition.
#print(b(10,20)) 

#c = lambda x,y : return x + y   return cannot be used inside a lambda expression.
#print(c(10,20))

# lambda function to return the sum of two numbers
add = lambda x, y: x + y
print(add(10, 20))#30
# lambda function to return the square of a number
square = lambda x: x ** 2
print(square(5)) #25
# lambda function to return the second element of a sequence
second = lambda x: x[1]
print(second([10, 20, 30]))#20
#tricky
a = lambda x : print(x+10), print(200), print(300)#200 300
print(a)       #<function <lambda> at ...>
print(type(a)) #<class 'tuple'>

#map 
a = [1,2,3,4,5,6]
m = map(lambda x : x**2, a) 
print(m) #<map object at ...>
print(type(m)) #<class 'map'>
l = list(m)     #1 4 9 16 25 36
print(l)

#filter 
a = [1,2,3,4,5,6]
f = filter(lambda x : x % 2 == 0, a)
print(f) #<filter object at ...>
print(type(f))#<class 'filter'>
l = list(f)
print(l)#[2, 4, 6]

#reduce 
import functools 
l = [1,2,3,4,5]
r = functools.reduce(lambda x,y : x+y, l) 
print(r)         #15
print(type(r))   #<class 'int'>

