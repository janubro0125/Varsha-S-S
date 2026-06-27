'''
print("1.Largest & Smallest in list:")
l = []
n = int(input("Enter length: "))
for i in range(n):
    elements = int(input("Enter elements: "))
    l.append(elements)
print(l)

highest = l[0]
smallest=l[0]
for i in l:
    if i>highest:
        highest=i
for j in l:
    if j < smallest:
        smallest = j
print("Highest value:",highest)
print("Smallest value:", smallest)
'''
'''
print("2.Second largest element:")
l = []
n = int(input("Enter length: "))
for i in range(n):
    elements = int(input("Enter elements: "))
    l.append(elements)
print(l)

highest = l[0]
second = l[0]

for i in l:
    if i > highest:
        highest = i

for j in l:
    if j > second and j != highest:
        second = j

print("Second highest value:", second)
'''
'''
print("3.Remove Duplicate element:")
l = []
n = int(input("Enter length: "))
for i in range(n):
    elements = int(input("Enter elements: "))
    l.append(elements)
print("Original List:",l)
new_list=[]
for i in l:
    if i not in new_list:
            new_list.append(i)
print("List after removing duplicates:",new_list)
'''
'''
print("4.Reverse a list:")
l=[]
n=int(input("Enter length:"))
for i in range(n):
    elements=int(input("Enter elements:"))
    l.append(elements)
l.sort()
print("OG list:",l)
reverse_list=[]
for i in range(len(l)-1,-1,-1):
    reverse_list.append(l[i])
print("Reverse list:",reverse_list)
'''
'''
print("5.Rotaion a list:")
l=[]
length=int(input("Enter length:"))
for i in range(length):
    elements=int(input("Enter elements:"))
    l.append(elements)
l.sort()
print("OG list:",l)
n=int(input("Enter number of positions to rotate:"))
n=n%len(l)
rotated_list=l[n:]+l[:n]
print("Rotated list:",rotated_list)
'''
'''
print("6.Common Elements:")
l1=[]
n1=int(input("Enter length of n1:"))

l2=[]
n2=int(input("Enter length of n2:"))

for i in range(n1):
    elements1=int(input("Enter elements n1:"))
    l1.append(elements1)
for j in range(n2):
    elements2=int(input("Enter elements n2:"))
    l2.append(elements2)
common=[]
for i in l1:
    for j in l2:
        if i==j and i not in common:
            common.append(i)
print("List 1:",l1)
print("List 2:",l2)
print("Common:",common)
'''
'''
print("7.Merge 2 lists:")
l1=[]
n1=int(input("Enter length of n1:"))

l2=[]
n2=int(input("Enter length of n2:"))

for i in range(n1):
    elements1=int(input("Enter elements n1:"))
    l1.append(elements1)
for j in range(n2):
    elements2=int(input("Enter elements n2:"))
    l2.append(elements2)
merge=[]
for k in l1:
    merge.append(k)
for m in l2:
    merge.append(m)
print("List 1:",l1)
print("List 2:",l2)
merge.sort()
print("Merged list:",merge)
'''
'''
print("8.Count even and odd:")
l=[]
n=int(input("Enter length of n:"))
for i in range(n):
    elements=int(input("Enter elements n:"))
    l.append(elements)
print(l)
even=0
odd=0
for elements in l:
    if elements%2==0:
        even+=1
    else:
        odd+=1
print("Even count:",even)
print("Odd count:",odd)
'''
'''
print("9.Sum & Average:")
l=[]
n=int(input("Enter length of n:"))
for i in range(n):
    elements=int(input("Enter elements n:"))
    l.append(elements)
print(l)
sum=0
for elements in l:
    sum+=elements
    average=sum/n
print("Sum of elements:",sum)
print("Average of elements:",average)
'''
'''
print("10.Sort a list:")
l=[]
n=int(input("Enter length of n:"))
for i in range(n):
    elements=int(input("Enter elements n:"))
    l.append(elements)
print(l)
'''
'''
print("11.Convert list to tuple:")
l=[]
n=int(input("Enter length of n:"))
for i in range(n):
    elements=int(input("Enter elements n:"))
    l.append(elements)
print(l)
t=tuple(l)
print(t)
'''
'''
print("12.Count Occcurence in Tuple:")
t=()
n=int(input("Enter length of n:"))
for i in range(n):
    elements=int(input("Enter elements n:"))
    t=t+(elements,)
print("Tuple:",t)
num=int(input("Enter number to check the count:"))
count=0
for j in t:
    if j==num:
        count+=1
print("Occurence of",num,"is:",count)
'''  
'''
print("13.Max & Min in Tuple:")
t=()
n=int(input("Enter length of n:"))
for i in range(n):
    elements=int(input("Enter elements n:"))
    t=t+(elements,)
print("Tuple:",t)
maximum=t[0]
minimum=t[0]
for i in t:
    if i>maximum:
        maximum=i
for j in t:
    if j < minimum:
        minimum = j
print("Maximum value:",maximum)
print("Minimum value:", minimum)
'''
'''
print("14.Compare 2 Tuple:")
t1=()
n1=int(input("Enter length of n1:"))
for i in range(n1):
    elements=int(input("Enter elements n1:"))
    t1=t1+(elements,)
print("Tuple 1:",t1)

t2=()
n2=int(input("Enter length of n2:"))
for i in range(n2):
    elements=int(input("Enter elements n2:"))
    t2=t2+(elements,)
print("Tuple 2:",t2)

if t1==t2:
    print("Tuple 1 & Tuple 2 are equal")
else:
    print("Tuple 1 & Tuple 2 are not equal")
'''
'''
print("15.Concatenate 2 Tuple:")
t1=()
n1=int(input("Enter length of n1:"))
for i in range(n1):
    elements=int(input("Enter elements n1:"))
    t1=t1+(elements,)
print("Tuple 1:",t1)

t2=()
n2=int(input("Enter length of n2:"))
for i in range(n2):
    elements=int(input("Enter elements n2:"))
    t2=t2+(elements,)
print("Tuple 2:",t2)

t3=t1+t2
print("Tuple 3:",t3)
'''
