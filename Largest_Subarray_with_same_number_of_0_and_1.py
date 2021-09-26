# Size of largest sub array with same number of 0 and 1
txt=input()
l=txt.count("1")
s=txt.count("0")
# print(l,s)
m=min(l,s)
print(m*2)