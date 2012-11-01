# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)

# Define "helper" functions

# Define event handler functions

# Create a frame

# Register event handlers

# Start frame and timers


x = 5

def c(y):
    return x + y

print c(1)


def b(x,y):
    x = x + y
    return x

print b(1,2)

def d(y):
    y = x + y
    return y

print d(1)


def a(y):
    global x
    x = x + y
    return y

print a(1)


count = 0

def square(x):
    global count
    count += 1
    return x**2

print square(square(square(square(3))))


a = 3
b = 6

def f(a):
    c = a + b
    return c

print f(1)


frame = simplegui.create_frame("My Frame", 100, 100)
frame.set_canvas_background("red")
frame.start()