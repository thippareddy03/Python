"""
Forloopprimenumber.py

This module contains code to print the prime numbers in a range 
of values
"""

start = 10
end = 25

for number in range(start, end+1):
    is_prime = True
    for index in range(2,number):
        if number % index == 0:
            is_prime = False
            break
    if is_prime:
            print(number)


"""
This module defines on how to find to find whether a number is even or not
"""

start = 10
end = 20

for number in range(start,end+1):
    if number % 2 == 0:
        print(number)

