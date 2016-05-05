import simplegui

def enter(txt):
    f=txt[0]
    if(f=="a" or f=="e" or f=="i" or f=="o" or f=="u"):
        print txt[1:]+f+"ay"
    else:
        print txt[0:]+"way"
        

frame=simplegui.create_frame("sample",300,300)
frame.add_input("enter text",enter,100)
frame.start()

