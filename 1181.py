import sys,math
# input= sys.stdin.readline

N= int(input())
li=[]

for _ in range(N):
    val= input()
    if val not in li:
        li.append(val)


#사전순,길이 짧은 순
li.sort(key=lambda x: (len(x),x))


for i in li:
    print(i)