import sys,math
input= sys.stdin.readline

T= int(input())

# for i in range(1,T+1):
#     sum=0
#     list=[]
#     a= input()
#     for j in range(0,len(a)):
#         if(j==0 and a[0]=='O'):
#             list.append(1)
#         elif(j==0 and a[0]=='X'):
#             list.append(0)
#         elif(a[j]=='O'):
#             list.append(list[j-1]+1)
#         else:
#             list.append(0)
    
#     for j in range(0,len(a)):
#         sum+=list[j]
    
#     print(sum)



# _는 사용하지 않는 변수
for _ in range(T):
    # 0~T-1
    total=0
    consecusive=0

    a= input().strip()

    for char in a:
        if char == 'O':
            consecusive+=1
            total+=consecusive
        else:
            consecusive=0

    print(total)