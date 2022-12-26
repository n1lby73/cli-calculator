#simple cli calculator using python 
#version ==> 1.0
print ("Simple calculator using python\nVersion 1.0\n\nOpearions allowed are:\n\n1. Addition = +\n2. Subtraction = -\n3. Multiplication = *\n4. Division = /\n5. Power = ^\n6. Binary = b\n7. Percentage = %")

print (" ")
#info from developer
print("NOTE: if you're looking for:\n1. Binary value of a single number\n2. percentage value of a single number \n\nkindly enter:\n'0' when the prompt ask for your second value \n'+' when it ask for your binary/percentage operation ")

print (" ")
#user's input
variable_1 = int(input("your first value: "))

variable_2 = int(input('your second value: '))

operation = input("your operation: ")

#Addition operatiion

if operation == "+":
    print (" ")
    print ("Your answer is: ", variable_1 + variable_2)
    print (" ")
    print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Subtraction operation

elif operation == "-":
    print (" ")
    print ("Your answer is: ", variable_1 - variable_2)
    print (" ")
    print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Multiplication operation 

elif operation == "*":
    print (" ")
    print ("Your answer is: ", variable_1 * variable_2 )
    print (" ")
    print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Division operation 
#output changed from float to intgers due to int 
#removed int cause it gives output like 0.5 as 0

elif operation == "/":
    print (" ")
    print ("Your answer is: ", variable_1 / variable_2)
    print (" ")
    print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Power operation 

elif operation == "^" :
    print (" ")
    print ("Your answer is: ", variable_1 ** variable_2)
    print (" ")
    print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Binary operation

elif operation == "b":
    print (" ")
    print ("You've choosen binary, basic operations allowed only:\n\n1. Addition = +\n2. Subtraction = -\n3. Division = /\n4. Multiplication = *\n5. Power = ^")
    print(" ")
    
#user operation for binary numbers

    binary_operation = input("your binary operation: ")
    
#Binary operation [addition]

    if binary_operation == "+":
        print (" ")
        print ("Your answer is: ", format(variable_1 + variable_2, "b"))
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Binary operation [subtraction]

    elif binary_operation == "-":
        print (" ")
        print ("Your answer is: ", format(variable_1 - variable_2 , "b"))
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Binary operation [division]

    elif binary_operation == "/":
        print (" ")
        print ("Your answer is: ", format(variable_1 / variable_2, "b"))
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Binary operation [multiplication]

    elif binary_operation == "*":
        print (" ")
        print ("Your answer is: ", format(variable_1 * variable_2, "b"))
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Binary operation [power]

    elif binary_operation == "^":
        print (" ")
        print ("Your answer is: " ,format(variable_1 ** variable_2, "b"))
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Invalid binary operation
    else:
        print (" ")
        print ("syntax error")
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Percentage operation

elif operation == "%":
    print (" ")
    print ("You've choosen percentage, basic operations allowed only:\n\n1. Addition = +\n2. Subtraction = -\n3. Division = /\n4. Multiplication = *\n5. Power = ^")
    print (" ")

#user operation for percentage

    percentage_operation = input("your percentage operation: ")
    
#Percentage operation [addition]

    if percentage_operation == "+":
        print (" ")
        print ("Your answer is: ", format(variable_1 + variable_2, "%"))
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Percentage operation [subtraction]

    elif percentage_operation == "-":
        print (" ")
        print ("Your answer is: ", format(variable_1 - variable_2 , "%"))
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Percentage operation [division]

    elif percentage_operation == "/":
        print (" ")
        print ("Your answer is: ", format(variable_1 / variable_2, "%"))
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Percentage operation [multiplication]

    elif percentage_operation == "*":
        print (" ")
        print ("Your answer is: ", format(variable_1 * variable_2, "%"))
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Percentage operation [power]

    elif percentage_operation == "^":
        print (" ")
        print ("Your answer is: " ,format(variable_1 ** variable_2, "%"))
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Invalid percentage operation
    else:
        print (" ")
        print ("syntax error")
        print (" ")
        print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")

#Inavlid operation
else:
    print (" ")
    print("syntax error")
    print (" ")
    print ("Your feedback and suggestion for improvement is highly welcomed\nProudly codded by n1l by73")