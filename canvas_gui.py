# This code will draw a text within the canvas when the
#button is clicked within the frame 
import simplegui

message="Hello"

def draw(canvas):
    canvas.draw_text(message,[20,50],20,"Blue")
    
def tick():
    global message
    message="Inside the canvas"
    
    
    
frame=simplegui.create_frame("sample_frame",200,200)

frame.set_draw_handler(draw)

frame.add_button("click",tick)

frame.start()
