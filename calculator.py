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
    
def div():
    global first, second
    first/=second
    output()
    
def mul():
    global first
    first*=second
    output()
    
def enter(inp):
    global second
    second=float(inp)
    output()
    
frame=simplegui.create_frame("sample frame",400,400)
frame.add_button("Print",output,100)
frame.add_button("Swap",swap,100)
frame.add_button("Add",add,100)
frame.add_button("Subtract",subtract,100)
frame.add_button("Division", div,100)
frame.add_button("Multiply", mul,100)
frame.add_input("Enter a value",enter,100)

frame.start()

    
   
