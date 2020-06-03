import math
def simplifyFrac(f):
    f=str(f)
    if "/" in f and f.count("/")==1:
        num,den=f.split("/")
        r=math.gcd(int(num),int(den))
        return str(int(int(num)/r))+"/"+str(int(int(den)/r))
def createFrac(num,den):
    return simplifyFrac(str(num)+"/"+str(den))
def floatToFrac(f):
    f=str(f)
    n=len(str(f[f.index('.')+1:]))
    return simplifyFrac(str(math.ceil(float(f)*math.pow(10,n)))+"/"+str(int(math.pow(10,n))))
def decToFrac(d):
    return str(d)+"/1"

def numerator(f):
    num,den=f.split("/")
    return int(num)
def denominator(f):
    num,den=f.split("/")
    return int(den)
def lcm(x, y):
    if x > y:
        greater = x
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm  
def add(f1,f2):
    r=lcm(denominator(f1),denominator(f2))
    s=numerator(f1)*(int(r/denominator(f1)))+numerator(f2)*(int(r/denominator(f2)))
    return simplifyFrac(str(s)+"/"+str(r))
def subtract(f1,f2):
    r=lcm(denominator(f1),denominator(f2))
    s=numerator(f1)*(int(r/denominator(f1))) - numerator(f2)*(int(r/denominator(f2)))
    return simplifyFrac(str(s)+"/"+str(r))
def multiply(f1,f2):
        return simplifyFrac(str(numerator(f1)*numerator(f2))+"/"+str(denominator(f1)*denominator(f2)))
def divide(f1,f2):
        return simplifyFrac(str(numerator(f1)*denominator(f2))+"/"+str(denominator(f1)*numerator(f2)))

    

    
    

        

        
    