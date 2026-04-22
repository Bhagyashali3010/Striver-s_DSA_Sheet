
# count = 0
# def nTimes(count, name, n):
#     if count == n:
#         return
#     print(name)
#     nTimes(count+1, name, n)

# nTimes(0,"bhagya", 5)

# def nlinear(c, n):
#     if c>n:
#         return
#     print(c)
#     nlinear(c+1,n)

# nlinear(1, 5)

# def nReverse (c,n):
#     if c==0:
#         return
#     print(c)
#     nReverse(c-1,n)

# nReverse(5,5)

# def backLinear(c,n):
#     if c==0:
#         return
#     backLinear(c-1, n)
#     print(c)

# backLinear(3,3)



# def backReverse(c, n):
#     if (c>n):
#         return
#     backReverse(c+1, n)
#     print(c)

# backReverse(1, 3)


# def sumOfNum(n):
#     if n==1:
#         return 1
#     return n + sumOfNum(n-1)
    

# print(sumOfNum(10))

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

print(factorial(4))