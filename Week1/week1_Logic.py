a = True
b = False
print not a
print not b

print "==="

p = True
q = True
x = not (p or not q)
print x

n = 123.4

x = (n%10)/10
print x

x = (n%100 - n%10)/10
print x

x = (n//10)%10
print x

def func1 (x):
	a = (-5 * (x ** 5)) + (69 * (x ** 2)) - 47
	return a

print func1(0)
print func1(1)
print func1(2)
	