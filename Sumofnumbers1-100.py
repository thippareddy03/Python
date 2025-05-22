"""
Sumofnumbers1-100.py
The purpose of this script is to add numbers 1 to 100
"""
First_Number = 1
total = 0

for sum in range(First_Number, 101):
    total += sum
print(total)

"""
Print all even numbers from 2 to 20.

"""

for numbers in range(2, 20):
    if numbers % 2 == 0:
        print(numbers)

"""
Print the multiplication table of a given number (e.g., 7) up to 10.
"""
multiplenumber = 7
for number in range (1, 11):
    result = multiplenumber * number
    print(result)