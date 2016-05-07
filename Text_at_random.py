#This program generates a text at random positions within the canvas

import simplegui
import random

message="Python is fun"
position=[0,0]
width=250
height=250

def draw(canvas):
    canvas.draw_text(message,position,20,"Blue")
    
def input_handler(inp):
    global message
    message=inp
 
def tick():
    global position
    global width
    global height
    x=random.randrange(10,width)
    y=random.randrange(10,height)
    position[0]=x
    position[1]=y

frame=simplegui.create_frame("testing",300,300)
frame.add_input("Enter value",input_handler,150)
timer=simplegui.create_timer(500,tick)
frame.set_draw_handler(draw)

timer.start()
frame.start()

