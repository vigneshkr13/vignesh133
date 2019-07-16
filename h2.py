aa=int(input())
bb=input("")
cc=list(bb.split(" "))
cc.sort(reverse=True)
bb=list(map(int,cc))
if sum(bb)==0:
  print("0")
else:
  dd="".join(cc)
  print(dd)
