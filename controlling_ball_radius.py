# Ball radius control - version 1

import simplegui

WIDTH = 300
HEIGHT = 300
ball_radius = 20
BALL_RADIUS_INC = 3

# Handler for keydown
def keydown(key):
    global ball_radius
    if(key==simplegui.KEY_MAP["down"]):
        ball_radius-=5
    
    # Add code here to control ball_radius

def keyup(key):
    global ball_radius
    if(key==simplegui.KEY_MAP["up"]):
        ball_radius+=5
# Handler to draw on canvas
def draw(canvas):
    # note that CodeSkulptor throws an error if radius is not positive
    canvas.draw_circle([300/2,300/2],ball_radius,2,"White","Blue")
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 300)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
