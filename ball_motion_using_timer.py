#This program generates the ball motion using timer

import simplegui

width=400
height=400
rad=20
dim=2
vel=[4,4]
pos=[width/2,height/4]

def draw(canvas):
    
    
    canvas.draw_circle(pos,rad,dim,"Red","Blue")

def tick():
    global pos,vel
    pos[0]+=vel[0]
    pos[1]+=vel[1]
    if(pos[0]<=rad):
        vel[0]=-vel[0]
    if(pos[0]>=width-rad):
        vel[0]=-vel[0]
    if(pos[1]<=rad):
        vel[1]=-vel[1]
    if(pos[1]>=height-rad):
        vel[1]=-vel[1]

frame=simplegui.create_frame("testing",width,height)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(100,tick)
timer.start()

frame.start()
