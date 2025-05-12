#To find out if a year is a leap year, you can use the following rules:
#The year must be divisible by 4.
#If the year is divisible by 100, it must also be divisible by 400 to be a leap year.
#If the year is divisible by 100 but not by 400, it is not a leap year.
year = 2000
if year % 4 == 0:
    if year % 100 == 0:
       if year % 400 != 0:
          print ( "Year is not leap" )
       else:
           print( "Year is leap" )
else:
     print( "Year is not leap" )

