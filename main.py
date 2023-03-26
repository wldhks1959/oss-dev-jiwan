c = [[0] * 15 for i in range(5)] # 한 열이 15인 리스트를 5행으로 만든다.
for i in range(5):
    d = list(input())
    d_len = len(d)
    for j in range(d_len):
        c[i][j] = d[j]

for i in range(15):
    for j in range(5):
        if c[j][i] == 0: #c[j][i]가 공백이라면 계속 진행
            continue;
        else:
            print(c[j][i], end='')

























