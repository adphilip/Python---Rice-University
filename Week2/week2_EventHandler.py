# Example of a simple event-driven program

# CodeSkulptor GUI module
import simplegui

# Event handler
def tick():
    print "tick!"
    
    
# Event handler
def poc():
    print "poc!"

# Register handler
timer = simplegui.create_timer(1000, tick)
timerPoc = simplegui.create_timer(2000, poc)

# Start timer
timer.start()
timerPoc.start()

##Stop timer
#timer.stop()

