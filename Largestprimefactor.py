#To find the prime factors of a number in Python, a common and efficient approach is:
#Repeatedly divide the number by 2 (the smallest prime) while it is even.
#Then check odd numbers from 3 up to the square root of the number.
#If after this process the remaining number is greater than 1, it is itself a prime factor.

number = 10
start = number - 1

while start > 1:
    if number % start == 0:
        # Checking if the number is prime or not
        is_prime = True
        index = 2
        while index < start:
            if start % index == 0:
                is_prime = False
                break
            index += 1
            if is_prime:
                print(start)
                break
    start -= 1

