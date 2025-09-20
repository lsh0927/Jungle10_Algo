N, C = map(int, input().split())

li = []
for _ in range(N):
    li.append(int(input()))

li.sort()

answer=0
start=1
end=li[-1]-li[0]

while start<=end:

    mid= (start+end)//2

    count=1
    cur=li[0]

    for i in range(1,len(li)):
        if cur + mid <= li[i]:
            cur= li[i]
            count+=1
        
    if count>=C:
        answer=mid
        start=mid+1
    else:
        end=mid-1

print(answer)