#This program will create a game in which the ball moves
#on the canvas and bounces back whenever it hits the wall

import simplegui
width=400
height=400
radius=20
pos=[width/4,height/2]
vel=[0.5,0.5]
def draw(canvas):
    pos[0]+=vel[0]
    pos[1]+=vel[1]
    if(pos[0]>=width-radius):
        vel[0]=-vel[0]
    if(pos[1]>=height-radius):
        vel[1]=-vel[1]
    if(pos[1]<=radius):
        vel[1]=-vel[1]
    if(pos[0]<=radius):
        vel[0]=-vel[0]
    canvas.draw_circle(pos,radius,2,"Red","Blue")
        
    
frame=simplegui.create_frame("testing",width,height)
frame.set_draw_handler(draw)

frame.start()
