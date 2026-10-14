#FOR LOOP PROBLEMS
#basic understanding
#1. print numbers from 1 to 10 in one line
i=1
for i in range(1, 11):
    print(i, end=" ")
    i+=1
print()
#2. print even numbers from 5 to 30 in one line
i=1
for i in range(5, 31):
    if i % 2 == 0:
        print(i, end=" ")
        i+=1
print()
#3. print odd numbers from 5 to 30 in one line
i=1
for i in range(5, 31):
    if i % 2 != 0:
        print(i, end=" ")
        i+=1
print()
#4. print numbers divisible by 5 from 1 to 30 in one line
i=1
for i in range(1, 31):
    if i % 5 == 0:
        print(i, end=" ")
        i+=1
print()
#5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
i=1
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")
        i+=1
print()
#6. sum of numbers from 10 to 25 
i = 10
sum = 0
while i <= 25:
    sum = sum + i
    i += 1
print(sum)
#7. sum of numbers in any list
numbers = [10, 20, 30, 40, 50]
total = 0
for i in numbers:
    total = total + i
print(total)
#8. multiplication table of a number 
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "*", i, "=", n * i)
#interview problems
#9. factorial 
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial =", fact)
#10. fibonacci 
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
#11. reverse a string
s = input("Enter a string: ")
reverse = ""
for i in range(len(s) - 1, -1, -1):
    reverse = reverse + s[i]
print("Reverse:", reverse)
#12. count vowels in a string
s = input("Enter a string: ")
count = 0
for i in s:
    if i in "aeiouAEIOU":
        count += 1
print("Vowel count:", count)
#13. count z's and y's in a string
s = input("Enter a string: ")
count = 0
for i in s:
    if i in "zZyY":
        count += 1
print("Count of z and y:", count)
# 14. check whether a number is prime number or not 
n = int(input("Enter a number: "))
if n < 2:
    print("Not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")



#WHILE LOOP PROBLEMS
#basic understanding
#print 1 to 10 with while loop
i = 1
while i < 11:
    print(i, end=" ")
    i = i + 1
#print even numbers from 1 to 10
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
#print numbers divisible by both 5 and 7 from 1 to 500 
i = 1
for i in range(1, 501):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")
        i += 1
print()
#interview problems
#count digits
n = int(input("Enter a number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print("Number of digits:", count)
#reverse a number
n = input("Enter a number: ")
reverse = ""
for i in range(len(n) - 1, -1, -1):
    reverse = reverse + n[i]
print("Reverse:", reverse)

#method two
n = input("Enter a number: ")
reverse = n[::-1]
print("Reverse:", reverse)
#palindrome number 
n = input("Enter a number: ")
reverse = n[::-1]
if n == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

#method two
n = int(input("Enter a number: "))
original = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
#palindrome string (without slicing, built in function)
s = input("Enter a string: ")
reverse = ""
for i in range(len(s) - 1, -1, -1):
    reverse = reverse + s[i]
if s == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
#armstrong number
n = int(input("Enter a number: "))
original = n
count = 0
temp = n
while temp > 0:
    count += 1
    temp = temp // 10
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10
if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#method two
n = input("Enter a number: ")
total = 0
for i in n:
    total = total + int(i) ** len(n)
if total == int(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")