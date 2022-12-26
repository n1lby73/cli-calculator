"""Simple cli calculator using python 
Version ==> 2.1
The update fixed some stuff:
	Added Quadratic operation """

#banner

print ("  ____________________---------------------------_____________________ \n |								      |\n | 		SIMPLE CALCULATOR USING PYTHON {Version 2.0}	      |\n |								      |\n | Opearions allowed are:   	  				      |\n |								      |\n |  (Addition = +) •••• (Subtraction = -) •••• (Multiplication = *)   |\n |								      |\n |       (Division = /) •••••• (Power = ^) •••••• (Binary = b)        |\n |								      |\n | 		(Percentage = %) •••• (Quadratic = q)			      |\n |								      |\n |  Note: If you're looking for the binary value of a single number   |\n |	input '0' as your second value and '+' as your binary	      |\n |				operation			      |\n --------------------______________________________--------------------\n\n")

#listing all function

#user input ==> main function

def user_input ():
	
	digit1 = int(input(" your first value: "))
	
	print (" ")
	
	sign = input(" your operation: ")
	
	print (" ")
	
	digit2 = int(input(" your second value: "))
	
	print (" ")
	
#result function

	def calc():
		print (" Answer ==>",all_operation(digit1,digit2,digit3))
		print(" ")
		print(" ——————————————————————••••••••••••••••••••••••——————————————————————\n")
		return user_input()
		
#binary operation function

	def binary_operation(b,o):
		ba = input(" your binary operation: ")
		print (" ")
		if ba == "+":
			return(format((b+o), "b"))
		elif ba == "-":
			return(format((b-o), "b"))
		elif ba == "*":
			return (format((b*o),"b"))
		elif ba == "/":
			return (format(int((b/o)),"b"))
		elif ba == "^":
			return(format(pow(b,o),"b"))
		else:
			return "SYNTAX ERROR !!!"

#quadratic operation function

    def quadratic_operation(a,b,c):

        return()

#operation function
			
	def all_operation(x,y,z=0):
		if sign == "+":
			return (x+y)
		elif sign == "-":
			return (x-y)
		elif  sign == "*":
			return (x*y)
		elif sign == "/":
			return (x/y)
		elif sign == "%":
			return ((x*y)/100)
		elif sign == "^":
			return pow(x,y)
		elif sign == "b":
			return binary_operation(x,y)
        elif sign == "q":
            digit3 = int(input(" your third value: "))
            return quadratic_operation(x,y,z)
		else:
			return "SYNTAX ERROR !!!"
			
	return (calc())

#equation function

	
user_input()
