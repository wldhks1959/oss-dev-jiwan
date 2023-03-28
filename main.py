chess=[]
chess=[input() for _ in range(8)] # 8열로 8행을 만든다.
w_cnt=0

for a in range(len(chess)):
    for b in  range(len(chess)):
        if a==0 or a%2==0: # 짝수열
            if b%2==0: # 짝수행
                if chess[a][b] != '.':
                    w_cnt += 1
        else: #홀수열
            if b!=0 and b%2==1: #홀수행
                if chess[a][b] != '.':
                    w_cnt += 1
print(w_cnt)
