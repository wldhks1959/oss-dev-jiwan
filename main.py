#T:테스트케이스 수 R: 반복 S: 문자열
P=[]
K=[]
T=int(input())

for i in range(T):
    P = [] # P를 비워주기
    R,S=input().split() # 반복 횟수와 문자열을 입력 받기
    R=int(R)
    for j in range(len(S)): # R만큼 문자열을 복제해서 P에 넣기
        P+=S[j]*R
    P=''.join(P)
    K.append(P)

for i in range(T):
    print(K[i])
