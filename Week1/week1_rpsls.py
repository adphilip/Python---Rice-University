# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
     # fill in your code below

   
    if number == 0:
        outName = "rock"
    elif number == 1:
        outName = "Spock"
    elif number == 2:
        outName = "paper"
    elif number == 3:
        outName = "lizard"
    elif number == 4:
        outName = "scissors"
    else:
        outName = "Error Input"
        
    return outName
   
##test sequence   
#print "convert to number  = ", number_to_name(3)  
#print "-4 mod 5", -4 %5
#print "4 mod 5", 4 %5

    
         
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        outName = 0
    elif name == "Spock":
        outName = 1
    elif name == "paper":
        outName = 2
    elif name == "lizard":
        outName = 3
    elif name == "scissors":
        outName = 4
    else:
        outName = "Error Input"
        
    return outName
    
##test print   
#print "convert to name  = ", name_to_number("scissors")



def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # compute difference of player_number and comp_number modulo five
    deltaModulo = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if deltaModulo == 1 or deltaModulo == 2:
        winner = "Player"
    elif deltaModulo == 3 or deltaModulo == 4:
        winner = "Computer"
    elif deltaModulo == 0:
        winner = "Draw"
    else:
        winner = "error"
    
    
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
   
    ## print results
    # print"\n ==== ", deltaModulo
    print "Player chooses ", name
    print "Computer chooses", comp_name
    print  winner, "wins!"
    print "\n"
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


#Player chooses rock 
#Computer chooses scissors 
#Player wins! 
