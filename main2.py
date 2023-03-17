import sys
total=[]
stu=[]
for i in range(1,31):
    total.append(i)

for i in range(28):
    stu.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,31): #1부터 30까지 번호 중 있으면 삭제해나간다.
    cmp=stu.count([i])
    if(cmp==1):
        total.remove(i)
print(min(total))
print(max(total))



