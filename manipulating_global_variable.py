#manipulating global variable


count=0

def increment():
    global count
    count+=1

def decrement():
    global count
    count-=1
    
def reset():
    global count
    count=0
    
def print_count():
    print count
    
print_count()
increment()
print_count()
increment()
print_count()
increment()
increment()
print_count()
decrement()
print_count()
reset()
print_count()
