#Basic calculator using if-else

user_input_1=float(input("Enter the first number:-"))
user_operation=str(input("Enter the operation you want to perform:-"))
user_input_2=float(input("Enter the second number:-"))
if user_operation=="+":
    print("The addition is",( user_input_1 + user_input_2))
elif user_operation=="-":
    print("The substraction of two numbers is",(user_input_1 - user_input_2))
elif user_operation=="*":
    print("The multiplication of two numbers is",(user_input_1*user_input_2))
elif user_operation=="/":
    print("The division of two numbers is",(user_input_1/user_input_2))
else:
    print("Please enter correct data")

