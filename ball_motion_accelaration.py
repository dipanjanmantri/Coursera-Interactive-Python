import simplegui

width=400
height=400

pos=[width/2,height/2]
rad=20
dim=2
vel=[0,0]

def draw(canvas):
    global pos,vel
    pos[0]+=vel[0]
    pos[1]+=vel[1]
    
    canvas.draw_circle(pos,rad,dim,"Red","Blue")

def keydown(key):
    global vel
    
    if(key==simplegui.KEY_MAP["left"]):
        vel[0]-=1
    if(key==simplegui.KEY_MAP["right"]):
        vel[0]+=1
    if(key==simplegui.KEY_MAP["up"]):
        vel[1]-=1
    if(key==simplegui.KEY_MAP["down"]):
        vel[1]+=1
        
frame=simplegui.create_frame("testing",width,height)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)
frame.start()

