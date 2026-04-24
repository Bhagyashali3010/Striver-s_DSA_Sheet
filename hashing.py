#basic hashing

# arr=[1,2,3,2,4,3]
# hash=[0]*5
# for i in range(len(arr)):
#     hash[arr[i]]+=1
# for i in hash:
#     print(i,"->",hash[i])

#charecter hashing

arr=['a','b','a','c','b']
hash=[0]*26
for i in range (len(arr)):
    hash[ord(arr[i])-ord('a')]+=1

print("n",'->',hash[ord('n')-ord('a')])
print("b",'->',hash[ord('b')-ord('a')])
print("c",'->',hash[ord('c')-ord('a')])