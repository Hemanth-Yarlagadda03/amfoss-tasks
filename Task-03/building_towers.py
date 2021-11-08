t = int(input())
kilos = list(map(int, input().split()))
towers = 0
n = set(kilos)
for i in n :
 if towers < kilos.count(i):
  towers = kilos.count(i)
print(towers,len(n))
