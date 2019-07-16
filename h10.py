    
aa,ba=map(int,input().split())
ca=list(map(int,input().split()))
da=list(map(int,input().split()))
e=0
if aa>ba:
    for i in range(ba):
        if((da[i]) in ca) and da.count(i)<=ca.count(i):
            e+=1
        else:
            e=0
if(e==ba):
    print("YES")
else:
    print("NO")
