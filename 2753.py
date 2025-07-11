import sys
input= sys.stdin.readline

year= int(input())

if(year%4!=0):
    print(0)
elif(year%100==0 & year%400!=0):
    print(0)
else:
    print(1)