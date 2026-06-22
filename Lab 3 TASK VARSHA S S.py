""""
print("Letter pattern")
for i in range(1,4):
    for j in range(1,6):
        if i==1 and j==1:
            print("@ ", end="")
        elif i==2 and j==2:
            print("@ ", end="")
        elif i==3 and j==3:
            print("@ ", end="")
        elif i==2 and j==4:
            print("@ ", end="")
        elif i==1 and j==5:
            print("@ ", end="")
        else:
            print("","",end="")
    print()
"""
"""
print("Loop 1.Integer and its sum for even and odd")
n=int(input("Enter a num:"))
even_sum=0
odd_sum=0
for i in range(1,n):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i

print("Sum of Even number:",even_sum)        
print("Sum of Odd number:",odd_sum)
"""
"""
print("Loop 2.Print Tables")
n=int(input("Enter a number:"))
for i in range(1,11):
    print(i,"*",n,"=",i*n)
"""
"""
print("Loop 3.Factorial")
num=int(input("Enter a number:"))

factorial=1
i=1

while i<=num:
    factorial=factorial*i
    i+=1
print("Factorial=",factorial)
"""
"""
print("Loop 4.Alphabets")
for i in range(65,91):
    print(chr(i),end=" ")
"""
"""
print("Loop 5.Reverse Alphabet")
for i in range(90,64,-1):
    print(chr(i),end=" ")
"""
"""
print("Loop 6.ASCII values")
for i in range(0,128):
    print(chr(i),"=",i)
"""
""""
print("Loop 7. Convert while to for")
m=5
n=10
'''
while (n>=1):
    print(m*n)
'''
for i in range(n,1,-1):
    print(m*n)
"""
"""
print("Loop 8.Harshad number")
n=input("Enter a number:")
sum_digits=0
for digits in n:
    sum_digits+=int(digits)
if int(n)%sum_digits==0:
    print(n,"Harshad number")
else:
    print(n,"Not Harshad number")
"""
"""
print("Loop 9.Divisor of given number")
num=int(input("Enter a number:"))

sum_divisors=0

for i in range(1,num+1):
    if num%i==0:
        sum_divisors+=i
print("Sum of divisors=",sum_divisors)
'''
print("Loop 11.Armstrong number")
n=input("Enter a number:")
'''
'''
print("Loop 12.Pattern")
for i in range(1,5):
    for j in range(i,6):
        print(" ",end="")
    for k in range(1,i):
        print("*",end="")
    print()
'''
'''
for i in range(1,6):
    for j in range(i,6):
        print(" ",end="")
    for k in range(1,i):
        print("* ",end="")
    print()
'''
'''
for i in range(1,6):
    for k in range(1,i):
        print("* ",end="")
    print()
'''
'''
for i in range(1,6):
    for k in range(i,6):
        print("* ",end="")
    print()
'''
'''
for i in range(1,6):
    for j in range(1,i):
        print(" ",end="")
    for k in range(i,6):
        print("* ",end="")
    print()
'''
'''
for i in range(1,6):
    for j in range(1,i):
        print(" ",end="")
    for k in range(i,6):
        print("*",end="")
    print()
'''
'''
for i in range(1,4):
    for j in range(i,4):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()

for i in range(2,0,-1):
    for j in range(i,4):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()
'''
'''
for i in [1,2,3,2,1]:
    for j in range(i,4):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()
'''


