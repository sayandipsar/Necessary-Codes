# Calculate permutation from a given string 
s=input()
l=len(s)
f=1
def fact(n):
    fa=1 
    for i in range(1,n+1):
        fa=fa*i 
    return(fa)
s1="".join(set(s))
for j in range(len(s1)):
    c=s.count(s1[j])
    if(c>1):
        f=f*fact(c)
res=(fact(l))/f 
print(res) #if we need integer result we have to write "int(res)" in place of "res" 