aa=int(input())
if(aa>=1 and aa<=100000):
  la=[]
  for i in range(0,aa):
    la.append(input())
  la.sort(reverse=True)
  for i in la:
    print(i,end="")
