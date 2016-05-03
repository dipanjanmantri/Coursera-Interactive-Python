import math

def smaller_sol(a,b,c):
    dis=(b**2-4*a*c)
    if(dis<0 or a==0):
        print "error: no solution"
        return
    if(dis==0):
        sol=(-b)/(2*a)
        return sol
    if(dis>0):
        sol1=(-b+math.sqrt(dis))/2*a
        sol2=(-b-math.sqrt(dis))/2*a
        if(sol1>sol2):
            return sol2
        else:
            return sol1
        
def test(a,b,c):
    fsol=smaller_sol(a,b,c)
    print fsol
    
test(1,2,3)
test(5,1,4)
test(1,10,2)
test(1,9,4)


    
        
    
    
