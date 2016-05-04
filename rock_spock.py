# mini project on rock paper scissors

import random
num=0

def name_to_number(name):
    if(name=="rock"):
        num=0
        return num
    elif(name=="Spock"):
        num=1
        return num
    elif(name=="paper"):
        num=2
        return num
    elif(name=="lizard"):
        num=3
        return num
    elif(name=="scissors"):
        num=4
        return num
    else:
        print "Error: Incorrect name"
        
        
name="" 
def number_to_name(number):
    if(number==0):
        name="rock"
        return name
    elif(number==1):
        name="Spock"
        return name
    elif(number==2):
        name="paper"
        return name
    elif(number==3):
        name="lizard"
        return name
    elif(number==4):
        name="Scissors"
        return name
    else:
        print "Error: Number not in range"
        
        
def rpsls(choice):
    print 
    print "The player's choice is ",choice
    number1=name_to_number(choice)
    rand_num=random.randrange(0,4)
    name1=number_to_name(rand_num)
    print "The computer's choice is ",name1
    diff=(number1-rand_num)%5
    if(diff==1 or diff==2):
        print "Player wins!"
    elif(diff==3 or diff==4):
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    
    
       
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
