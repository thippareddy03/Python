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





Max_Number = 20
Start = 5
Until Start < Max_Number
do
if Max_Number % Start == 0
result = start
#Need to find out if this result is Prime or not
Prime_Start == 2
untill Prime_Start =< result
if result % Prime_Start != 0
Prime_Number = result
end if
Prime_Start = prime_Start + 1
end if
start = start + 1
print Prime_Number

