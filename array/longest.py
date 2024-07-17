
nums = [0,3,2,5,4,6,1,1]
def longestConsecutive(nums):
    res=set(nums)
    longest=0
    for num in nums:
        if num-1 not in res:
            length=1
            while(num+length) in res:
                length+=1
            longest=max(length,longest)
    return longest
   


print (longestConsecutive(nums))


def longest(nums):
    res=set(nums)
    longest=0
    for num in res:
        if (num-1) in res:
            while (nums+length) in res:
                length+=1
            longest=max(length,longest)
    return longest



