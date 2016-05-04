#this program implements a frame and a timer
import simplegui

counter=0

def increment():
    global counter
    counter+=1
    
def tick():
    increment()
    print counter
    
def reset_timer():
    global counter
    counter=0
    
frame=simplegui.create_frame("sample_frame",200,200)
frame.add_button("click to reset the timer", reset_timer)

timer=simplegui.create_timer(2000,tick)

frame.start()
timer.start()
