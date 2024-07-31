nums = [-2,1,-3,4,-1,2,1,-5,4]

# 6 = 6+2 = 8, 8-1 =7, 7+3 = 2 , 2+4 =6

# [-2,1,-3,4]

# sum  - num[i] = new value

# new value = new value  - num [(i)+1] 
# new value = max(new value, new value - num [ (i)+1 +1])
# def maxSubArray(nums):
#     if len(nums) ==0:
#         return None
#     max_sum =float("-inf")
#     for i in range(len(nums)):
#         max_sum = nums[i] + max(max_sum , maxSubArray(nums[1:]))
#     return max_sum

# print(maxSubArray(nums))



def maxSubArray (nums):
    if len(nums) ==0:
        return None
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum+num)
        max_sum = max(max_sum,current_sum)
    return max_sum

print(maxSubArray(nums))



def maxSubArray(nums):
    if not nums:
        return 0

    # Initialize dp array where dp[i] represents the maximum sum of subarray ending at index i
    dp = [0] * len(nums)
    dp[0] = nums[0]
    max_sum = dp[0]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
        max_sum = max(max_sum, dp[i])

    return max_sum