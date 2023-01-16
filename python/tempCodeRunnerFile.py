n=1
a=0

while a!=1:
    if n%2 == 0:
        n/=2
    else:
        n=n*3+1
    if n==1:
        a=1
    print(n)
