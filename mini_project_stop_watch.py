import simplegui
import time

val=0
current_time=0
f=""

def tick():
    global val,f
    #print "So far the handler has executed ",val,"times"
    f=format(val)
    val+=1
    

def draw(canvas):
    canvas.draw_text(f,[70,150],24,"White")

 
def draw1(canvas):
    
    
def start():
    timer.start()
    
def stop():
    timer.stop()

def reset():
    timer.stop()
    global val
    val=0
    frame.set_draw_handler(draw1)
    

def format(t):
    s1=""
    s2=""
    s3=""
    s4=""
    t3=0
    if(t==0):
        return "0:00.0"
    else:
        t1=t%10
        t2=t/10
        if(t2<=9):
            s2="0"+str(t2)
        if(t2>=10 and t2<60):
            s2=str(t2)
        if(t2==60):
            t2=t2%60
            if(t2<=9):
                s2="0"+str(t2)
            if(t2>=10):
                s2=str(t2)
        if(t2>60):
            t3=t2/60
            s3=str(t3)
            t2=t2%60
            if(t2<=9):
                s2="0"+str(t2)
            if(t2>=10):
                s2=str(t2)
            
            
        
            
        if(t3>0):
            return s3+":"+s2+"."+str(t1)
        else:
            return s2+"."+str(t1)
        
   
   
        
    
    
frame=simplegui.create_frame("testing",300,300)
frame.set_draw_handler(draw)
frame.add_button("start",start,150)
frame.add_button("stop",stop,150)
frame.add_button("reset",reset,150)



timer=simplegui.create_timer(100,tick)
#timer.start()
frame.start()

format(321)

