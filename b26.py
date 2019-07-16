aa,bb=map(int,input().split())
for i in range(aa+1,bb):
  for z in range(2,i):
    if(i%z==0):
      break
  else:
      print(i,end=" ")
