import sys
N=int(input())
a=[]
count=0

a=map(int,sys.stdin.readline().split())
v=int(input())
a=list(a)

for i in range(0,N):
    if(a[i]==v):
        count+=1
print(count)