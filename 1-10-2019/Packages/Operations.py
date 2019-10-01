def addition(a,b):
    c=a+b
    print(c)
    
def prime(a):
    fact=0
    for i in range(1,a+1):
        if a%i==0:
            fact=fact+1
    if fact==2:
           print("true")
    else:
          print("false")
        
        