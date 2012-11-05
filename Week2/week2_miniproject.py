# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

http://www.codeskulptor.org/#user4-ZMeb9CO1PA-0.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

# initialize global variables used in your code
num_range = 100
max_tries = 7

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    global max_tries

    num_range = 100
    max_tries = 7
    
    #how many tries 
    counter = 0
    
    #number to be guessed
    new_number = 0
    
    #init again
    init()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range    
    global max_tries
    
    num_range = 1000
    max_tries = 10
    
    #init again
    init()
    
def init():
    #init game
    global counter
    global new_number
    counter = 0 
    
    new_number =random.randint(0, num_range)
    
    print "\nNew game! Range is from 0 to", num_range
    print "Number of remaning guesses: ", max_tries
    print "\n"
    
def logic_find(guess_int):
    # find teh number
    
    if guess_int > new_number :
        print "Lower!"
    elif guess_int < new_number :
        print "Higher!"
    elif guess_int == new_number :
        print "Yes you did it! The number is:", new_number
    else:
        print "Error 2 in application! Please debug!"
    
    
def get_input(guess):
    # main game logic goes here	
    
    guess_int = int(guess)
    
    global counter
    counter += 1
    
    #check the number
    if counter <= max_tries :
        print "Guess number is:", guess_int
        print "Remaining times:",max_tries - counter 
        logic_find(guess_int)
    else:
        print "You lost! The number was:",new_number
        #restart application in ELSE
        if num_range == 100:
            range100()
        elif num_range == 1000:
            range1000()
        else:
            print "Error 1 in application! Please debug!"
           

    
# create frame
frame = simplegui.create_frame("Guess Number", 200, 200)

# register event handlers for control elements
button100 = frame.add_button("Range (0,100)", range100)
button1000 = frame.add_button("Range (0,1000)", range1000)

inp = frame.add_input("Number", get_input, 50)

#init game
init()

# start frame
frame.start()

# always remember to check your completed program against the grading rubric
