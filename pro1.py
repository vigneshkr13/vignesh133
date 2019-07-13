ma=int(input())
qa=[]
for i in range(0,ma):
  ra=input()
  qa.append(ra)
sa=[]
for i in zip(*qa):
  if(i.count(i[0])==len(i)):
    sa.append(i[0])
  else:
    break
print(''.join(sa))
