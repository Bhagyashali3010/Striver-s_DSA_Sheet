# Two Sum : Check if a pair with given sum exists in Array

nums = [3,2,4]
target = 6
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


arr=[]
dicti={}
for i in range(len(nums)):
    if nums[i] not in dicti:
        dicti[nums[i]]=i
        print(dicti)
    if (target-nums[i]) in dicti and i!=dicti[target-nums[i]]:
        print(i,dicti[target-nums[i]] )
        arr.append(dicti[target-nums[i]])
        arr.append(i)
        break
print (arr)

