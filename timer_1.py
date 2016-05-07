#Playing with timer
import simplegui

val=0

def timer_handler():
    global val
    
    print val
    val+=1

def start_handler():
    timer.start()
    
def reset_handler():
    global val
    val=0
    
def stop_handler():
    timer.stop()
    
frame=simplegui.create_frame("testing",300,300)
frame.add_button("start",start_handler,150)
frame.add_button("reset",reset_handler,150)
frame.add_button("stop",stop_handler,150)

timer=simplegui.create_timer(2000, timer_handler)

frame.start()

