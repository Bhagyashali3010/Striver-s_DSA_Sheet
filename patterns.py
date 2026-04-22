# for i in range(5):
#     for j in range (5):
#         print("*", end="")
#     print()


#2
# for i in range(5):
#     for j in range (i+1):
#         print("*", end="")
#     print()


#3
# for i in range(5):
#     for j in range (i+1):
#         print(j+1, end="")
#     print()


#4
# for i in range(5):
#     for j in range (i+1):
#         print(i+1, end="")
#     print()


#5
# for i in range (5):
#     for j in range (5-i):
#         print("*", end="")
#     print()


#6
# for i in range (5):
#     for j in range (5-i):
#         print(j+1, end="")
#     print()


#7
# n=5
# for i in range (n):
#     for j in range (n-(i+1)):
#         print(" ", end="")
#     for j in range((2*i)+1):
#         print("*", end="")
#     for j in range (n-(i+1)):
#         print(" ", end="")
#     print()


#8
# n=5
# for i in range (n):
#     for j in range (i):
#         print(" ", end="")
#     for j in range(((2*n)-(2*i))-1):
#         print("*", end="")
#     for j in range (i):
#         print(" ", end="")
#     print()


#9
# n=5
# for i in range (n):
#     for j in range (n-(i+1)):
#         print(" ", end="")
#     for j in range((2*i)+1):
#         print("*", end="")
#     for j in range (n-(i+1)):
#         print(" ", end="")
#     print()
# for i in range (n):
#     for j in range (i):
#         print(" ", end="")
#     for j in range(((2*n)-(2*i))-1):
#         print("*", end="")
#     for j in range (i):
#         print(" ", end="")
#     print()



#10
# n=5
# for i in range(2*n):
#     if i>=n:
#         for j in range((2*n)-(i+1)):
#             print("*", end="")
#         print()
#     else:
#         for j in range(i+1):
#             print("*", end="")
#         print()



#11
# n=5
# num=1
# for i in range (n):
#     if i%2==0:
#         num=1
#     else:
#         num=0   
#     for j in range (i+1):
#         print (num, end="")
#         if num==0:
#             num=1
#         elif num==1:
#             num=0
#     print()



#12
n=4
for i in range(n):
    for j in range(i+1):
        print(j+1, end="")
    for j in range((2*n)-(2*(i+1))):
        print(" ", end="")
    for j in range(i+1):
        print(j+1, end="")
    print()