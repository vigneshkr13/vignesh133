aa=int(input())                       
bb=list(map(int,input().split()))   
l=[]
for i in range(len(bb)):
    if i == bb[i]:                
        l.append(str(bb[i]))
if len(l)!=0:
    print(" ".join(l))               
else:
    print('-1')
