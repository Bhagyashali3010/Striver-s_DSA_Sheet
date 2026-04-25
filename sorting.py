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

arr=[34,52,3,68,23,8]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1]=arr[j+1], arr[j]

print(arr)