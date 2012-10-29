#operations
import math

# Python modules - extra functions implemented outside basic Python
import simplegui	# access to drawing operations for interactive applications
import random   	# functions to generate random numbers


#import prints
print "PI = ", math.pi
print "Choice = ", random.choice([1,2,3,4])

#tests
num = 46
val = num // 6
val2 = num % 10
print 'val = ', val, "val2 = ", val2

#convert int in strings

val = 56.55
valStr = str(val)
# use concat "+" operator for strings
print "String = " + valStr