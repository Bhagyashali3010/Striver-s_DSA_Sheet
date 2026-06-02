#largest number

# arr=[3,4,1,2,78,9,-54,34]
# maxi=0
# for i in arr:
#     if i>maxi:
#         maxi=i

# print(maxi)


#second largest number

#--Brute force
# arr=[5,5,5]
# arr.sort()
# for i in range(len(arr)-1, -1,-1):
#     if arr[i]>arr[i-1]:
#         print(arr[i-1])
#         break
# else:
#     print(-1)

#--Optimal approach
# max1=float('-inf')
# max2=float('-inf')
# for i in range(len(arr)):
#     if arr[i]>max1:
#         max2=max1
#         max1=arr[i]
#     elif arr[i]>max2 and arr[i]!=max1:
#         max2=arr[i]

# if max2==float('-inf') or len(arr)<2:
#     print(-1)
# else:
#     print(max2)


#is array sorted

# arr=[1,4,6,45,2,78]
# for i in range(1, len(arr)):
#     if arr[i]<arr[i-1]:
#         print(False)
#         break
# else:
#     print(True)
    

#Remove duplicate from a sorted array

nums=[1,1,2]

#Bbrute force
uni=nums[0]
count=1
i=1
while i<len(nums):
    if nums[i]==uni:
        nums.remove(nums[i])
        i=i
        print(nums)
    else:
        uni=nums[i]
        count+=1
        i+=1
print(count, nums)

#optimal
i=0
for j in range(1, len(nums)):
    if nums[i]!=nums[j]:
        i+=1
        nums[i]=nums[j]
print(i+1, nums)