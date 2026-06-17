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
n=list[int(input("Enter set of integers:").split())]
even_sum=0
odd_sum=0
for i in n:
    if i%2==0:
        even_sum+=1
    else:
        odd_sum+=1

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
print("Loop 4.Alphabets")
for i in range(65,91):
    print(chr(i),end=" ")
"""
"""
print("Loop 5.Reverse Alphabet")
for i in range(90,64,-1):
    print(chr(i),end=" ")
"""
