import sys

N=int(input())
A=[]
A=map(int,sys.stdin.readline().split(maxsplit=N-1))
A=list(A)
for i in range(N):
    if(A[i]==min(A)):
        print(A[i], end=" ")
    elif (A[i]==max(A)):
        print(A[i], end=" ")