# Sum of digits until get a single digit
n = int(input())


def calsum(n):
    s = 0
    while(n > 0):
        s = s+(n % 10)
        n = n//10
    return(s)


while(n > 9):
    n = calsum(n)
print(n)
