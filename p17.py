import sys
num=input()
aa=list(map(int,num.split()))
k=aa[1]
h=input()
flag=0
ss=list(map(int,h.split()))
for i in range(0,len(ss)-1):
	for j in range(i+1,len(ss)):
		if ss[i]+ss[j]==k:
			print("yes")
			flag=1
			sys.exit()
print("no")	
