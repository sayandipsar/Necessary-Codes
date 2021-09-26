# firstline contains the number of integer
# secondline contain the n numbers 
#calculate absolute difference between each two numbers and calculate the sum
n=int(input())
l1=list(map(int,input().split()))
c=0
for i in range(n-1):
    c=c+abs(l1[i]-l1[i+1])
print(c)