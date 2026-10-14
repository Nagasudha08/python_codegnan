# no.of digits in a num using while loop
# n = input("Enter a number: ")
# reverse = ""
# for i in range(len(n) - 1, -1, -1):
#     reverse = reverse + n[i]
# print("Reverse:", reverse)

n = int(input("Enter a number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print("Number of digits:", count)