#This program will move a circle thorughout the canvas when the
#keyboard keys are pressed, its the basic of animation

import simplegui

width=800
height=800
pos=[width/2,height/2]
radius=20

def keydown(key):
    if(key==simplegui.KEY_MAP["left"]):
        pos[0]-=4
    if(key==simplegui.KEY_MAP["right"]):
        pos[0]+=4
    if(key==simplegui.KEY_MAP["up"]):
        pos[1]-=4
    if(key==simplegui.KEY_MAP["down"]):
        pos[1]+=4
def draw(canvas):
    canvas.draw_circle(pos,radius,10,"Red","Blue")

frame=simplegui.create_frame("testing",width,height)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

frame.start()

