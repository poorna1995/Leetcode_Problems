nums=[10,21,23,432]
# print(nums[:])

# # res=[]

# # len(nums) =4 
# # multoplu len(nums)-1
# # res[0] = nums[1]*nums[2]*nums[3]
# # num[:j]


def product(nums):
    res=[1]*len(nums)
    prefix=1
    for i in range(len(nums)):
        res[i]=prefix
        prefix*=nums[i] 
    postfix=1
    for i in range(len(nums)-1,-1,-1):
        res[i]*=postfix
        postfix*=nums[i]
    return res

print(product(nums))