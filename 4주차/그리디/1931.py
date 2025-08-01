import sys
input= sys.stdin.readline

N=int(input())
meeting=[]

for _ in range(N):
    a,b=map(int,input().split())
    meeting.append((a,b))


meeting.sort(key=lambda x: (x[1],x[0]))
#print(meeting)

curEnd=meeting[0][1]
curStart=meeting[0][0]
cnt=1

for i in range(1,N):
    nextStart=meeting[i][0]
    nextEnd=meeting[i][1]

    if nextStart==nextEnd:
        cnt+=1

    elif nextStart>=curEnd:
        curEnd=nextEnd
        cnt+=1

    else:        
        continue

print(cnt)