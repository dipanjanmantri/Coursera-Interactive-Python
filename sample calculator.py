# This code swaps prints, swaps, adds and subtracts the global values
import simplegui


first=10
second=20

def output():
    print "first = ",first
    print "second = ",second
    print ""
    
def swap():
    global first, second
    first, second=second, first
    print "After swap: "
    output()
    
def add():
    global first, second
    first+=second
    print "After addition: "
    output()
    
def subtract():
    global first, second
    first-=second
    print "After subtraction: "
    output()
    
frame=simplegui.create_frame("sample frame",200,200)
frame.add_button("Print",output,100)
frame.add_button("Swap",swap,100)
frame.add_button("Add",add,100)
frame.add_button("Subtract",subtract,100)

frame.start()

    
   
