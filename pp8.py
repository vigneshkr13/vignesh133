from math import gcd
na, qa = map(int, input().split())
x = list(map(int, input().split()))
ra = []
for _ in range(qa):
    u, v = map(int, input().split())
    ra.append(x[u-1]) if u == v else ra.append(gcd(x[u-1], x[v-1]))
for i in ra:
    print(i)
