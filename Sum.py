"""
Addition of two numbers a Twist
1. Using a method, pass two variables and find the sum of two numbers.

Test case:
Number 1 – 20
Number 2 – 20.38
Sum = 40.38

There were a total of 4 test cases.
Once you compile 3 of them will be shown to you and 1 will be a hidden one.
You have to display error message if numbers are not numeric.
"""
def Sum (a , b):
     sum = float(0)
     sum = a + b
     return sum

a = int(input("Enter First Int varible :"))
b = float(input("Enter Second float variable :"))

c = Sum(a , b)
print("Sum of First and Second variable :",c)
