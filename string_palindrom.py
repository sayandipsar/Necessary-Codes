s = input()
# Revserse a string
rev = ""
for i in s:
    rev = i+rev
print(rev)
# Check Palindrom or not
if(s == rev):
    print("Palindrom")
else:
    print("Not Palindrom")
