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

# nums=[1,1,2]

# #Bbrute force
# uni=nums[0]
# count=1
# i=1
# while i<len(nums):
#     if nums[i]==uni:
#         nums.remove(nums[i])
#         i=i
#         print(nums)
#     else:
#         uni=nums[i]
#         count+=1
#         i+=1
# print(count, nums)

# #optimal
# i=0
# for j in range(1, len(nums)):
#     if nums[i]!=nums[j]:
#         i+=1
#         nums[i]=nums[j]
# print(i+1, nums)


#Rotate array by k

# nums=[1,2,3,4,5]
# k=3

# for i in range(k):
#     ele=nums.pop()
#     nums.insert(0,ele)
# print(nums)


#Optimal appraoch 

# k=k%len(nums)
# nums.reverse()
# print(nums)
# print(nums[:k])
# print(nums[k:])
# nums[:k]=reversed(nums[:k])
# print
# nums[k:]=reversed(nums[k:])
# print(nums)

#Left rotate by one

# t_arr=[]
# temp = nums[0]
# for i in range(1, len(nums)):
#     nums[i-1]=nums[i]

# nums[-1]=temp
# print(nums)


#Move zeros to the end
nums=[0,4,6,0,6,0,0,8]

#brute force:

# c=0
# i=0
# while i<(len(nums)):
#     if nums[i]==0:
#         nums.remove(nums[i])
#         c+=1
#     else:
#         i+=1
# for j in range(c):
#     nums.append(0)
# print(nums)

#optimal

# c=0
# for i in range(len(nums)):
#     if nums[i]!=0:
#         nums[c]=nums[i]
#         c+=1
# while c<len(nums):
#     nums[c]=0
#     c+=1
# print(nums)


#linear search

# nums=[2,3,5,7,4,3]
# target=3

# for i in range(len(nums)):
#     if nums[i]==target:
#         print(i)
#         break

#Union of 2 sorted array

# nums1=[1,2,4,5]
# nums2=[2, 3, 5, 7]


# nums=[]
# i=0
# j=0
# l1=len(nums1)
# l2=len(nums2)
# while i<l1 or j<l2:
#     if nums1[i] not in nums:
#         nums.append(nums1[i])
    # i+=1
    # if nums2[j] not in nums:
    #     nums.append(nums2[j])
    # j+=1
    # print(nums)



#Find missing element

arr=[1,3,4,2,6]

#brute force :

# for i in range(1,len(arr)+2):
#     if i not in arr:
#         print(i)
#         break


#better approach: using hash map

# hash=[0]*(len(arr)+2)

# for i in range(len(arr)):
#     hash[arr[i]]+=1
   
# for j in range(1, len(hash)):
#     if hash[j]==0:
#         print(j)


#optimal - natural number addition formula

# n=len(arr)+1
# summ=(n*(n+1))/2

# s=sum(arr)
# print(int(summ-s))


#Maximum consecutive once

# arr=[1,0,1,0,1,0,1,0,1,1,1,1]

# c=0
# maxi=0
# for i in range(len(arr)):
#     if arr[i]==1:
#         c+=1
#         maxi=max(maxi,c)
#     else:
#         c=0
# print(maxi)


#Single number

# nums=[1,3,3,4,9,1,4]

# dict={}

# for i in range(len(nums)):
#     n=nums[i]
#     if n in dict:
#         dict[n]+=1
#     else:
#         dict[n]=1
# print(dict)

# for k in dict:
#     if dict[k]==1:
#         print(k)



# Longest Subarray with given Sum K(Positives)

nums = [10, 5, 2, 7, 1, 9]
k = 15  

# if sum(nums)==k:
#     print(len(nums))
# elif sum(nums)==0:
#     print(0)

# brute force

# summ=0
# c=0
# maxi=0
# i=0
# while i<len(nums):
#     summ+=nums[i]
#     c+=1
#     if summ==k:
#         i=i
#         maxi=max(maxi, c)
#         c=0
#         summ=0
#     else:
#         i+=1
# print(maxi)

# optimal

# nums = [10, 5, 2, 7, 1, 9]
# k = 15 

# maxi=0
# l=0
# r=0
# summ=nums[0]

# while r<len(nums):
#     while l<=r and summ>k:
#         summ-=nums[l]
#         l+=1
#     if k==summ:
#         maxi=max(maxi, r-l+1)
#     r+=1
#     if r<len(nums):
#         summ+=nums[r]
        
# print(maxi)


