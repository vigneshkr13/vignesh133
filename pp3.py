    
aa,ba=input().split()
l=len(aa) if len(aa)<len(ba) else len(ba)
d=abs(len(aa)-len(ba))
count=d
for i in range(l):
  if(len(ba)==1 and ba[i] in aa):
    break
    
  if(aa[i]!=ba[i]):
    count+=1
print(count)
