
#reverse
# n=345600
# r=0
# while n>0:
#     x=(n%10)
#     r=x+r*10
#     n=n//10
#     print(r)

#palindrom
# n=23329
# c=n
# r=0
# while n>0:
#     x=(n%10)
#     r=x+r*10
#     n=n//10
# if c==r:
#     print(True)
# else:
#     print(False)


#GCD
# n1=12
# n2=9
# if n1<n2:
#     n=n1
# else:
#     n=n2
# for i in range (n,0,-1):
#     if n1%i==0 and n2%i==0:
#         print(i)
#         break


#amstrong
# n=156
# num=n
# c=0
# while n>0:
#     c+=1
#     n=n//10
# # print(c)
# sum=0
# n=num
# while n>0:
#     x=n%10
#     sum+=x**c
#     n=n//10
#     # print(sum)
# if num==sum:
#     print(True)
# else:
#     print(False)

# import math

# n=36
# arr=[]
# for i in range(1,int(math.isqrt(n))+1):
#     if n%i==0:
#         arr.append(i)
#         if i!=(n//i):
#             arr.append(n//i)
#     print(arr)

import math

n=71
for i in range(2, int(math.isqrt(n))+1):
    if n%i==0:
        print(False)
        break
else:
    print(True)
    