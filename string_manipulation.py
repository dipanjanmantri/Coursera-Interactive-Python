# String manipulation

def convert_string(dollars,cents):
    if(dollars>1 and cents>1):
        print dollars,"dollars","and",cents+1,"cents"
    if(dollars>1 and cents==1):
        print dollars,"dollars","and",cents,"cent"
    if(dollars>1 and cents==0):
        print dollars,"dollars"
    if(dollars==1 and cents>1):
        print dollars,"dollar","and",cents+1,"cents"
    if(dollars==1 and cents==1):
        print dollars,"dollar","and",cents,"cent"
    if(dollars==1 and cents==0):
        print dollars,"dollar"
    if(dollars==0 and cents>1):
        print cents,"cents"
    if(dollars==0 and cents==1):
        print cents,"cent"
    
        

def convert(money):
    dollars=int(money)
    cents=int(100*(money-dollars))
    #print dollars," dollars "," and ",cents," cents"
    convert_string(dollars,cents)

    



convert(20.45)
convert(20.01)
convert(20.00)
convert(20)
convert(1.45)
convert(1.00)
convert(1)
convert(0.45)
convert(0.01)
convert(1.01)

