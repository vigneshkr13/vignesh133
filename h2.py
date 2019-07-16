x=int(input())
if(x>=1 and x<=100000):
  l=[]
  for i in range(0,x):
    l.append(input())
  l.sort(reverse=True)
  for i in l:
    print(i,end="")
