a=True
while 1 :
    n=int(input())
    list=[]
    result=0
    if n == -1 :
        break
    else :
        for i in range(1,n):
            if n%i==0:
                list.append(i) #list에 n의 약수를 추가.
    #list에서 약수들을 더해서 n이 나오면 완전수
    for i in range(len(list)):
        result+=list[i]
    if result==n:
        # n은 완전수
        print(f"{n} = {' + '.join(map(str,list))}")
    else :
        print(f'{n} is NOT perfect.')
        
