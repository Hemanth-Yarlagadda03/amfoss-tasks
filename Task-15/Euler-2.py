import sys

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    s = 0
    a = 0
    b = 1
    while b < n:
        if b%2==0:    
            s += b
        a,b = b,a+b
    print(s)

