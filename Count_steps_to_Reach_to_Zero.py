# count steps to reach the number to zero 
# substruct by one if it is odd else divide by 2 and then increse step by one and
# at last print how many steps required to reach to zero0
n=int(input())
c=0 
while(n!=0):
    if(n%2==0):
        n=n//2
    else:
        n=n-1
    c=c+1 
print(c)