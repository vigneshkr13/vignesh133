na,qa=list(map(int,input().split()))
lis=list(map(int,input().split()))
for i in range(qa):
  u,v=list(map(int,input().split()))
  print(min(lis[u-1:v]))
