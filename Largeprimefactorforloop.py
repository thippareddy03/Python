"""
Largeprimefactorforloop.py

This module defines on how to find out the large prime factor of a number
 using for loop and range
"""

number = 13195

for factor in range(number, 1, -1):
        if number % factor == 0:
            # Need to find out whether the index in prime or not
            is_prime = True
            for index in range(2, factor):
                if factor % index == 0:
                    is_prime = False
                    break
            if is_prime:
                 print(factor)
                 break