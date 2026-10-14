# # While loop
# x = 1 
# while x <= 10:
#     print(x, end=' ')# infinte 1 1 1..
# print()
x = 1 
while x <= 10:
    print(x, end=' ')#1 3 5 7 9 
    x += 2
print()
x = 1
while x <= 10:
    print(x, end=' ')#1 2 4 8
    x *= 2
print() 
x = 10 
while x >= 0:          
    print(x, end=' ')
    x -= 2 
print() # 10 8 6 4 2 0
x = 10 
while x > 0:           #no = 0, because // last value is 0
    print(x, end=' ')
    x //= 2 
print() #10 5 2 1 

#else 
x = 1 
while x < 5:
    if x % 2 == 1:
        x += 1
        continue 
    print(x, end=' ')
    x += 1 # 2 4
else:
    print('Loop completed successfully') # loop completed successfully
print()
x = 1 
while x < 5:
    if x == 4:
        break 
    print(x, end=' ')#1 2 3 
    x += 1
else:
    print('Loop completed successfully')
print()

#nested loops
for x in range(1,4):
    for y in range(4,7):
        print((x,y), end=' ')
print('\n')#(1,4) (1,5) (1,6) (2,4) (2,5) (2,6) (3, 4) (3, 5) (3, 6) 
for x in range(1,3):
    for y in range(3,5):
        for z in range(5,7):
            print((x,y,z), end=' ')#(1, 3, 5) (1, 3, 6) (1, 4, 5) (1, 4, 6) (2, 3, 5) (2, 3, 6) (2, 4, 5) (2, 4, 6) 

#matrix 
matrix = [ [4,5,6], [1,2,3], [7,8,9]]
m = matrix
#print matrix row-wise
print("Row-wise:")
for row in range(len(m)):
    for col in range(len(m[0])):
        print(m[row][col], end=' ')
    print()
#print matrix col-wise
print("\nCol-wise:")
for col in range(len(m[0])):
    for row in range(len(m)):
        print(m[row][col], end=' ')
    print()