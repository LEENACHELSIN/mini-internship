#Task-1
number=int(input("enter a number"))
if number %2==0:
    print("The number is an even.")
else:
    print("the number is an odd.")

#Task-2
age=int(input("enter your age"))
if age >=18:
    print("you are eligibel")
else:
    print("you are not eligibel")

#Task-3
number=int(input("enter your number"))
if number %3==0 and number%5==0:
    print("fizz and buzz")
elif number %3==0:
    print("fizz.")
elif number %5==0:
    print("buzz.")
else:
    print('not divided')
               
