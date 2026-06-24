'''
print("1.Reverse string")
String=input("Enter a string:")
print(String[::-1])
'''
'''
print("2.String Palindrome")
word=input("Enter a word:")
reverse=word[::-1]
if reverse==word:
    print(word,"Palindrome")
else:
    print(word,"Not Palindrome")
'''
'''
print("3.Count vowels and consonants")
word=input("Enter a word:")
vowels=0
consonants=0
for ch in word:
    if ch.isalpha():
        if ch in 'aeiou':
            vowels+=1
        else:
            consonants+=1
print("Vowels:",vowels)
print("Consonants:",consonants)
'''
'''
print("4.Remove Duplicate Character")
string=input("Enter a string:")
duplicate=""
for ch in string:
    if ch not in duplicate:
        duplicate+=ch
print(duplicate)
'''
'''
print("5.First Non-Repeated Character")
s=input("Enter a string: ")
for ch in s:
    if s.count(ch) == 1:
        print("First non-repeated character:", ch)
        break
'''
'''
print("6.Count of each charater")
s = input("Enter a string: ")

for ch in s:
    print(ch, "=", s.count(ch))
'''
'''
print("7.Anagram")
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagram")
else:
    print("Not Anagram")
'''
'''
print("8.Replace spaces with hyphen")
string=input("Enter a string:")
print(string.replace(" ","-"))
'''
'''
print("9.Count number of words")
string=input("Enter a string:")
string.split()
print("Number of words:",len(string))
'''
'''
print("10.Longest word in sentence")
sentence=input("Enter a sentence:")
words=sentence.split()
longest=""
for long_word in words:
    if len(long_word)>len(longest):
        longest=long_word
print("Longest word:",longest)
'''
'''
print("11.Capitalize first letter")
string=input("Enter a string:")
print(string.title())
'''
'''
print("12.Remove special characters")
string=input("Enter string:")
result=""
for chr in string:
    if chr.isalnum():
        result+=chr
print(result)
''' 
'''
print("13.Remove special characters")
string=input("Enter a string:")
upper=0
lower=0
for ch in string:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
print("Upper:",upper)
print("Lower:",lower)
'''
'''
print("14.Check whether string contains only digits")
string=input("Enter string:")
if string.isdigit():
    print("Contains only digits")
else:
    print("Contains other characters")
'''
'''
print("15.Most frequent character")
string=input("Enter a string:")
frequent=""
count = 0
for ch in string:
    if string.count(ch) > count:
        count=string.count(ch)
        frequent= ch
print("Most frequent character:", frequent)
'''
'''
print("16.Replace whitespaces")
string=input("Enter a string:")
print(string.replace(" ",""))
'''
'''
print("17.Count occurences of Sub string")
string=input("Enter a string:")
sub_string=input("Enter substring:")
print(string.count(sub_string))
'''
'''
print("18.Rotational string")
string1=input("Enter str1:")
string2=input("Enter str2:")
if len(string1)==len(string2) and string2 in (string1+string1):
    print("Rotational")
else:
    print("Not Rotational")
'''
'''
print("19.Compress a string")
'''
'''
print("20.Longest Repeating Substring")

'''
