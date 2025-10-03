import sys
input= sys.stdin.readline

N=int(input())
meeting=[]

for _ in range(N):
    meeting.append(list(map(int,input().split())))

meeting.sort(key= lambda x: (x[1],x[0]))

cnt=1
tmpS=meeting[0][0]
tmpE=meeting[0][1]

for i in range(1,N):

    if tmpE<=meeting[i][0]:
        # 새로운 회의 진행
        tmpE=meeting[i][1]
        cnt+=1
    else:
        continue

print(cnt)
    


