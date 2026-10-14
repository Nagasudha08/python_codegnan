#number patterns
# n = 4
# for r in range(1, n + 1):          # outer loop → rows
#     for c in range(1, r + 1):      # inner loop → numbers
#         print(c, end=" ")
#     print()                         # next row

#reverse
# n = 4
# for r in range(1, n + 1):
#     for c in range(r, 0, -1):
#         print(c, end=" ")
#     print()
# same number in same row
# n = 4
# for r in range(1, n + 1):
#     for c in range(r):
#         print(r, end=" ")
#     print()
#for all 1 
# n = 4
# for r in range(1, n + 1):
#     for c in range(r):
#         print(1, end=" ")
#     print()
#triangle
# n = 5
# for r in range(1, n + 1):
#     # spaces
#     for c in range(n - r):
#         print(" ", end="")
#     # numbers
#     for c in range(1, r + 1):
#         print(c, end=" ")
#     print()   # inside the outer loop
# print()

#floyd's triangle

# n=4
# num=1
# for i in range(1, n+1):
#     for j in range(i):
#         print(num, end=" ")
#         num+=1
#     print()

#pascal triangle
n = 5
row = [1]
for i in range(n):
    print(row)
    new_row = [1]
    for j in range(len(row) - 1):
        new_row.append(row[j] + row[j + 1])
    new_row.append(1)
    row = new_row