"""
Consider the below series :
0, 0, 2, 1, 4, 2, 6, 3, 8, 4, 10, 5, 12, 6, 14, 7, 16, 8
This series is a mixture of 2 series all the odd terms in this series form even numbers in
ascending order and every even terms is derived from the previous  term using the formula (x/2)

Write a program to find the nth term in this series.

The value n in a positive integer that should be read from STDIN the nth term that is
calculated by the program should be written to STDOUT. Other than the value of the nth term no
other characters /strings or message should be written to STDOUT.

For example if n=10,the 10 th term in the series is to be derived from the 9th term in the series.
The 9th term is 8 so the 10th term is (8/2)=4. Only the value 4 should be printed to STDOUT.

You can assume that the n will not exceed 20,000.
"""
N = int(input("Enter nth term of the series :"))

if N % 2 == 1 :
    series_position = int((N + 1) / 2)
    series_value = int((series_position - 1) * 2)
    print("Series value of nth term: ",series_value)

elif N % 2 == 0 :
    series_position = int(N / 2)
    series_value = int(series_position - 1)
    print("Series value of nth term: ",series_value)
