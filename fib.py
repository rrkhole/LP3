F=[-1]*100
F[0]=F[1]=1
def DP(n):
    if(F[n]!=-1):
        return F[n] 
    else:
        return DP(n-1)+DP(n-2)

def recursive(n):
    if n==0:
        return 1
    if n<=2:
        return n 
    return recursive(n-1)+recursive(n-2) 

def iterative(n):
    if n==0:
        return 1
    if n<=2:
        return n 
    a=1 
    b=1 
    c=0
    for i in range(2,n+1):
        c=a+b 
        temp=b 
        b=c 
        a=temp 
    return c 

print(iterative(10))
print(recursive(10))
print(DP(10))