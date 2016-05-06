import simplegui
import random

count=7
secret_number=0
upper_limit=100

def input_guess(inp):
    n=int(inp)
    
def game_1():
    global count
    global upper_limit
    upper_limit=100
    count=7
    new_game(upper_limit)
    
def game_2():
    global count
    count=10
    global upper_limit
    upper_limit=1000
    new_game(upper_limit)
    
    
def new_game(n):
    global secret
    secret=random.randrange(0,n)
    print "The secret number is in the range of [0, ",n,")"
    
def input_guess(inp):
    global count
    count-=1
    n=int(inp)
    print "Guess was ",n
    
    if(secret_number>n):
        print "The secret number is higher"
    elif(secret_number<n):
        print "The secret number is lower"
    else:
        print "Correct"
    print "You have ",count," guesses left"
    if(count==0):
        print "Game over, you consumed all the chances"
        print ""
        new_game(upper_limit)    
    
    print ""
    
    
    
        
    
    
    

frame=simplegui.create_frame("testing",300,300)
frame.add_button("Range is [0, 100)",game_1,100)
frame.add_button("Range is [0, 1000)",game_2,100)
frame.add_input("Guess a number",input_guess,100)

new_game(upper_limit)

frame.start()

