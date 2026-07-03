# Two Sum : Check if a pair with given sum exists in Array

# nums = [3,2,4]
# target = 6
# arr=[]
# seen={}

# for i in range (len(nums)):
#     if nums[i]>target:
#         pass
#     elif nums[i]<=target:
#         seen.add(nums[i])
#         num=target-nums[i]
#         print(num)
#         if num in seen and (nums.index(num)) != i:
#             if (nums.index(num)) > i:
#                 arr.append(i)
#                 arr.append(nums.index(num))
#                 break
#             else:
#                 arr.append(nums.index(num))
#                 arr.append(i)
#                 break
#         else:
#             pass
# print(arr)


# arr=[]
# dicti={}
# for i in range(len(nums)):
#     if nums[i] not in dicti:
#         dicti[nums[i]]=i
#         print(dicti)
#     if (target-nums[i]) in dicti and i!=dicti[target-nums[i]]:
#         print(i,dicti[target-nums[i]] )
#         arr.append(dicti[target-nums[i]])
#         arr.append(i)
#         break
# print (arr)


#Sort the array containing (0's, 1's, and 2's)
# Used the Dutch National Flag Alogorithm

# nums=[0,1,0,2,1,0,2,1]
# low=0
# mid=0
# high=len(nums)-1

# while mid<=high:
#     print(nums)
#     if nums[mid]==0:
#         nums[low], nums[mid]= nums[mid], nums[low]
#         low+=1
#         mid+=1
#     elif nums[mid]==1:
#         mid+=1
#     else:
#         nums[high], nums[mid]= nums[mid], nums[high]
#         high-=1
# print(nums)

#Majority element 

# nums = [7, 0,2,7, 0, 1, 7, 7, 2, 7, 7,7]
#better
# dicti={}
# maxi=0
# for i in range(len(nums)):
#     if nums[i] not in dicti:
#         dicti[nums[i]]=1
#     else:
#         dicti[nums[i]]+=1
#         maxi=max(maxi, dicti[nums[i]])
#         if maxi>=len(nums)/2:
#             print(nums[i])

#optimal
#Moore's Voting Algo

# cnt=0
# ele=0
# for num in nums:
#     if cnt==0:
#         cnt+=1
#         ele=num

#     elif ele==num:
#         cnt+=1
#     else:
#         cnt-=1
 
# if nums.count(ele)>len(nums)/2:
#     print(ele)



#Maximum Subarray Sum (Kadane's Algo)

# nums = [-1,2, 3, 5, -2, 7, -4]
# maxi=float('-inf')
# summ=0
# start=nums[0]
# for i in range(len(nums)):
#     if summ==0:
#         start=i
#     summ+=nums[i]
        
#     if summ>maxi:
#         maxi=summ
#         end=i

#     if summ<0:
#         summ=0
# print(maxi)
# for i in range (start, end+1):
#     print(nums[i])


# Stock Buy And Sell

# prices = [1,2,4,2,5,7,2,4,9,0,9]
# i=0
# j=1
# maxi=0
# while j<len(prices):
#     if prices[i]>=prices[j]:
#         i=j
#         j+=1
#     else:
#         profit=prices[j]-prices[i]
#         maxi=max(maxi, profit)
#         j+=1
#     print(i, j, maxi)
    

# optimal approach

# mini=float('inf')
# profit=0

# for i in range(len(prices)):
#     if prices[i]<mini:
#         mini=prices[i]
#     else:
#         profit=prices[i]-mini
#     print(profit)


# Rearrange array elements by sign

nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
# arr=[]
# p=[]
# n=[]

# for num in nums:
#     if num>0:
#         p.append(num)
#     else:
#         n.append(num)
# for i in range(len(n)):
#     arr.append(p[i])
#     arr.append(n[i])
# print(arr)             

    
#optimal
arr=[0]*len(nums)
p=0
n=1
for num in nums:
    if num>0:
        arr[p]=num
        p+=2
    else:
        arr[n]=num
        n+=2
    print(arr)

