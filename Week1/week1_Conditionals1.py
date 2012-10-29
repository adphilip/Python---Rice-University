#if

a = 5

print a > 6 
def functionConditionals (a,b):
	if (a > 5):
		print "On a"
	elif (b > 5):
		print "On b"
	else:
		print "In the end"
		
functionConditionals(3,6)
functionConditionals(6,6)
functionConditionals(-6,-6)


#another function

def functionModulo3(a):
	if a % 2:
		print "First a"
	elif (a % 2) == False:
		print "Second"
	
functionModulo3(5)
functionModulo3(4)