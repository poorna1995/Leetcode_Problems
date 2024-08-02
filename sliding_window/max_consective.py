nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
from collections import Counter
def maxConsecutive(nums,k):
    if len(nums) < k:
        return 0
    max_cons=[]
    max_length =0
    
    for index,num in enumerate(nums):
        print(f'index:{index} and num:{num}')
        if nums[index]==1:
            index+=1
            max_cons.append()
            max_length =max (max_length,len(max_cons))
        else:
            nums[index] == 1
            max_cons.append()
            max_length =max (max_length,len(max_cons))




def maxConsecutive(nums, k):
    left = 0
    max_length = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        # Shrink the window until the number of zeros is <= k
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        # Calculate the max length of the window
        max_length = max(max_length, right - left + 1)
    
    return max_length
            


print(maxConsecutive(nums,k))
