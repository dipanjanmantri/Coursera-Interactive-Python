#This program plays an animation which generates a circle
#at an interval of 100 ms

import simplegui

radius=2

def draw(canvas):
    canvas.draw_circle([500,500],radius,2,"Red")


def tick():
    frame.set_draw_handler(draw)
    global radius
    radius+=1
    if(radius>500):
        timer.stop()
    
    
frame=simplegui.create_frame("testing",1000,1000)
timer=simplegui.create_timer(100,tick)

timer.start()
frame.start()

