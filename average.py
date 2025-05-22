maths = 20
physics = 10
chemistry = 10
average = (maths + physics + chemistry) / 3
#print(average) and need to print in which grade he was assigned to.

if average <= 100 and average >= 90:
    print("Grade A")
elif average < 90 and average >= 80:
    print("Grade B")
elif average < 80 and average >= 70:
    print("Grade C")
elif average < 70 and average >= 60:
    print("Grade D")
elif average < 60 and average >= 0:
    print("Grade E")
else:
    print("Marks are beyond control")


n = 50

if n % 2 == 0:
    if n == 2 and n >= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print ("Not Wierd")
else:
    print("Weird")