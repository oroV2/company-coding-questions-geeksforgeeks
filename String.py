"""
String with a Twist


1. The program will recieve 3 English words inputs from STDIN

1.These three words will be read one at a time, in three separate line
2.The first word should be changed like all vowels should be replaced by %
3.The second word should be changed like all consonants should be replaced by #
4.The third word should be changed like all char should be converted to upper case
5.Then concatenate the three words and print them

For example if you print how are you then output should be h%wa#eYOU.

You can assume that input of each word will not exceed more than 5 chars
"""
a = input("Enter First String: ")
b = input("Enter Second String: ")
c = input("Enter Third String: ")
vowels = ['a','e','i','o','u']

d = list(a)
e = list(b)

i = 0
j = 0

while i < len(a):
    if d[i] in vowels:
	    d[i] = '%'
    i += 1

while j < len(b):
    if e[j] not in vowels:
        e[j] = '#'
    j += 1

a = ''.join(map(str, d))
b = ''.join(map(str, e))

print("\nString First: ",a)
print("String Second: ",b)
print("String Third: ",c.upper())

d = a + b + c.upper()

print("\nFinal String: ",d)
