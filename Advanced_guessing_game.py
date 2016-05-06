#Advanced number guessing game 

import simplegui
import random
import math

secret_number=0
upper_limit=100
count=7
count100=0
count1000=0

def input_guess(inp):
    global count
    global count100
    global count1000
    if(count==7):
        count100=count
    if(count==10):
        count1000=count
    count-=1
    n=int(inp)
    print "Guess was ",n
    if(secret_number>n):
        print "Higher"
        print "you have ",count," chances left"
        print ""
    if(secret_number<n):
        print "Lower"
        print "You have ",count," chances left"
        print ""
    if(secret_number==n):
        print "Correct"
        print ""
        reset_count()
        new_game()
        return 
    if(count==0):
        print "Game over, you consumed all the chances"
        print ""
        reset_count()
        new_game()
        return
        
   
def reset_count():
    global count
    global count100
    global count1000
    if(count100==7):
        count=count100
    if(count1000==10):
        count=count1000

        
def game100():
    global upper_limit
    global count
    count=7
    upper_limit=100
    new_game()
    
def game1000():
    global upper_limit
    global count1000
    global count
    count=10
    upper_limit=1000
    new_game()
    
        
        
def new_game():
    global count
    global count100
    global count1000
    global upper_limit
    global secret_number
    secret_number=random.randrange(0,upper_limit)
    print "The secret number is in the range of [0,",upper_limit,")"
    print "You have ",count," guesses left"
    print ""
    
    
frame=simplegui.create_frame("sample",300,300)
frame.add_button("Range is [0, 100)",game100,100)
frame.add_button("Range is [0, 1000)",game1000,100)
frame.add_input("Guess a number",input_guess,100)


new_game()
frame.start()





