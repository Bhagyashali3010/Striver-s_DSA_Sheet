#selection sort

# arr=[34,52,3,68,23,8]
# n=len(arr)
# for i in range(len(arr)):
#     mini=i
#     for j in range(i, len(arr), 1):
#         if arr[j]<arr[mini]:
#             arr[j], arr[mini]=arr[mini], arr[j]
# print(arr)



#bubble sort

# arr=[34,52,3,68,23,8]
# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j], arr[j+1]=arr[j+1], arr[j]

# print(arr)


#insertion sort

arr=[9,11,23,3,7,20]

for i in range(len(arr)):
    j=i
    while (j>0 and arr[j-1]>arr[j]):
            arr[j], arr[j-1]=arr[j-1], arr[j]
            j-=1
    print(arr)