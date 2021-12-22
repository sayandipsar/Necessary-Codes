# Read a string containing alphabets and numerics
s = input()
# store numbers in list
num = [int(i) for i in s.split() if i.isdigit()]
# Store alphabets in list
alp = [str(j) for j in s.split() if j.isalpha()]

n = 0
for i in num:
    n = n+i
a = ""
for j in alp:
    a += j

print(a)
print(n)
