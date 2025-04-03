"""Now there might be a case where the elements of the list are not decided already. This means that number of elements and the values are not determined. In this case, we will pass values as parameters which in turn will act as a list i.e. collection of values.

*args: It is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list."""
# User defined function taking the 
# values as input
def Product(*arguments): 
	p = 1
	for i in arguments:
		
		# Multiplying each and every element
		p *= i 
	
	# Printing the final answer which 
	# is their multiplication
	print(p) 

# Passing values that we want in our list
Product(4, 5, 1, 2) 
