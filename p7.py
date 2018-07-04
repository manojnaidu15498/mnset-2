import math
N = int(input())
temp = N
while N>0:
    i=N%10
    x=math.pow(i,3)
    sum=sum+x
    N=N//10
    if temp==sum:
        print('yes')
        break
    else:
        print('no')
