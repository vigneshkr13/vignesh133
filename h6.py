import sys
aa=int(input())
bb=list(map(int,input().split()))
for i in bb:
    if(bb.count(i)>1):
        print(i)
        sys.exit()
print("unique")
