import sys
T=int(input())
a=[]
b=[]
for i in range(T):
    A,B=map(int,sys.stdin.readline().split())
    a.append(A)
    b.append(B)

for i in range(T):
    print(a[i]+b[i])

