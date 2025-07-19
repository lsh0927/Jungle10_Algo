import sys,math
input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교


N,C= map(int,input().split())
li=[]
for _ in range(N):
    li.append(int(input()))

li.sort()

def bin_search(start,end):
    while start<=end:
        mid=(start+end)//2

        cur= li[0]
        count=1

        for i in range(1,len(li)):
            if li[i]>=cur +mid:
                count+=1
                cur=li[i]

        if count>=C:
            global answer
            start=mid+1
            answer=mid
        else:
            end=mid-1

start=0
end=li[-1]-li[0]
answer=0

bin_search(start,end)
print(answer)