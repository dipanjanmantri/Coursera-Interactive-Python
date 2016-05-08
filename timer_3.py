import simplegui

time=0
click=0

def handler():
    global time, click
    timer.start()
    click+=1
    if(click==2):
        timer.stop()
        print "The time difference between the two clicks: ",str(time),"secs"
    
def tick():
    global time
    time+=1
    
frame=simplegui.create_frame("testing",300,300)
timer=simplegui.create_timer(1000,tick)
frame.add_button("click",handler,150)



frame.start()
