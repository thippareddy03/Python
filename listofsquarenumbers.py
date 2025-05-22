"""
Create a list of squares of numbers from 1 to 15.
"""

for number in range (1, 16):
    result = number * number
    print(result)

"""
Count the number of vowels in a given sentence.
"""

Sentence = "Count the number of vowels in a given sentence"

vowels = "aeiouAEIOU"
count = 0

for char in Sentence:
    if char in vowels:
        #print(char)
        count += 1
print("Number of vowels in the sentence:", count)