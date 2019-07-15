na,ma=map(str,input().split())
t=0
if len(na)>len(ma):
	na,ma=ma,na
v=0
while v<len(na):
	  t+=(ord(ma[v])-ord(na[v]))
	  v+=1
for v in range(v,len(ma)):
	  t+=ord(ma[v])-ord('a')+1
print(t)
