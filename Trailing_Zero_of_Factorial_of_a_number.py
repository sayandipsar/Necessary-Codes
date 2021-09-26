# Calculate trailing zeroes of n!
n=int(input())
m=0
while(n>=5):
    m=m+int(n/5)
    n=n//5
print(m)
    