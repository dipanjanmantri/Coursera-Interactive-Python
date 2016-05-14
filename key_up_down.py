import simplegui

current_key=" "

def keydown(key):
    global current_key
    current_key=chr(key)
    
def keyup(key):
    global current_key
    current_key=" "
    
def draw(canvas):
    canvas.draw_text(current_key,[15,25],24,"White")

frame=simplegui.create_frame("testing",40,40)
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

frame.start()
