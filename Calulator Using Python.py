#Calculator Using Python 

#Take Two numbers as an input from the user 
num_1 = input("Enter the number 1: ")
num_2 = input("Enter the number 2: ")

#Enter the Operation you want to perform 
operation = input("Enter the operation: ")

if operation == "+":
    print (int(num_1) + int(num_2) )
elif operation == "-":
    print (int(num_1) - int(num_2))
elif operation == "*":
    print (int(num_1) * int(num_2))
elif operation == "/":
    print (int(num_1) / int(num_2))
else:
    print ("Enter the valid Operation")
    