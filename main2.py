C=int(input())
result=[]
for _ in range(C):
    total=0 # 학생들의 점수를  total에 넣는다.
    avr=0 # 학생들 점수 평균
    cnt=0 # 평균이 넘는 학생들을 셈
    score=[] # 학생수와 점수를 입력받는 score 리스트
    score.clear() # score에 있는 원소들을 제거한다.
    score=list(map(int,input().split()))
    #score리스트에 학생수와 점수를 입력받는다.
    N=int(score[0]) # score에 첫번째 원소인 학생수 : N
    score.pop(0) # score 첫번째 원소를 제거
    #N이라는 변수에 학생수를 대입/ score의 첫번째 인덱스를 삭제
    for i in range(len(score)):
        total+=score[i]
    avr=total//N
    #score길이만큼 반복,total에 점수들을 추가.
    for i in range(len(score)):
        if avr<score[i]:
            cnt+=1
    result.append(round(cnt/N*100,3))

for i in range(C):
    print("%0.3f%%"%(result[i]))


