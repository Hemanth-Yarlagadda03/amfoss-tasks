import numpy as np
n,k = map(int, input().split())
d = list(map(int,input().strip().split()))[:n]
p = list(map(int,input().strip().split()))[:k]
out = np.array([0]*7)
n1=len(d)
n2=len(p)
d.sort()
p.sort()
if d[n1-1] > p[n2-1] :
  print('NO')
for i in range(n1-1):
  if d[i]< p[n2-1]  :
print('YES')
    count = np.sum(p[i]>d[i])
    out[i] = count
print(out)   
