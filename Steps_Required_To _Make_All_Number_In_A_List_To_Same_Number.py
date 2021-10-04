# How many Steps required to make all elements of an array to a same number
a=list(map(int,input().split()))
l=len(a)
c=0
while((len(set(a)))>1):
    a.sort()
    for i in range(l-1):
        a[i]=a[i]+1
    print(a)
    c=c+1
print("Value of count "+str(c))
        
        