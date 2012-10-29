#define Function
def triangle_area(base, height):
    area = base * height
    return area

print 'Area = ',triangle_area(3,5)

#call a function inside of other

def quatrele(a,b,h):
    q = a + triangle_area(b,h)
    return q

print quatrele(1,4,5)

#hello
def hello_function():
    print "Print in hello function!"
    
    
hello_function()    
  