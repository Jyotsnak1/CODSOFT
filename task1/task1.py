print("CALCULATOR")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.MODULO")
print("SELECT ANY OPERATION")
operation=int(input())
if operation==1:
    first_number=int(input("Enter first value:"))
    second_number=int(input("Enter second value:"))
    print("The Sum of given values are: ",first_number+second_number)
elif operation==2:
    first_number=int(input("Enter first value:"))
    second_number=int(input("Enter second value:"))
    print("The difference of given values are: ",first_number-second_number)
elif operation==3:
    first_number=int(input("Enter first value:"))
    second_number=int(input("Enter second value:"))
    print("The multiplication of given values are: ",first_number*second_number)
elif operation==4:
    first_number=int(input("Enter first value:"))
    second_number=int(input("Enter second value:"))
    print("The division of given values are: ",first_number/second_number)
elif operation==5:
    first_number=int(input("Enter first value:"))
    second_number=int(input("Enter second value:"))
    print("The remainder of given values are: ",first_number%second_number)
else:
    print("Invalid Operation!! please enter valid operation")

