import sys,math
input= sys.stdin.readline

li=[]
for _ in range(9):
    li.append(int(input()))


li.sort()
total=sum(li)
val= total-100
flag=False

# 두명의 키의 합이 val이 되는 경우를 찾아 li에서 삭제
for i in range(0,8):
    if flag:
        break
    for j in range(i+1,9):
        if li[j]+li[i] == val:
            #큰값먼저? 혹은 값이 겹칠때
            li.remove(li[j])
            li.remove(li[i])
            flag=True
            break

for n in li:
    print(n)