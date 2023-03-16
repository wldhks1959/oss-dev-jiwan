import sys
N,X=map(int,input().split())
A=[]
A=map(int,sys.stdin.readline().split(maxsplit=N-1))
A=list(A)
for i in range(N):
    if(A[i]<X):
        print(A[i] ,end=" ")