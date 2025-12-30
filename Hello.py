a=18
b=12
gcd=1
n=2
while n<=min(a,b):
    if a%n==0 and b%n==0:
        gcd=gcd*n
        a=a//n
        b=b//n
    else:
        n=n+1
print(" GCD is",gcd)



        

