# program written from scratch to provide functionality of a calculator
num1=int(input("\nType 1st number : "))
operation=input("Enter operation to be performed (+ , - , * , / ) : ")
num2=int(input("\nType 2nd number : "))
if operation == '+':
    print("\n Total : ",num1+num2)
elif operation == '-':
    print("\n Total : ",num1-num2)
elif operation == '*':
    print("\n Total : ",num1*num2)
elif operation == '/':
    print("\n Total : ",num1/num2)
else:
    print("\nIncorrect Choice")

