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
'''
'''
print("5.First Non-Repeated Character")
s = input("Enter a string: ")
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
print("8.Replace spaces with hyphen")
