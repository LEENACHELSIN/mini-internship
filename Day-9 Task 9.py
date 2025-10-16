#Task1
print("Calculator")
num1=int(input("Enter your first number"))
num2=int(input("enter your secound number"))
operator=input("select the operator ")
if operator == "+":
    print (num1+num2)
elif operator == "-":
    print (num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("invalid operator")
#Task2
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul (x,y):
    return x*y
def div (x,y):
    return x/y


