nums = [1,7,3,6,5,6]

def pivot_index(nums):
    total = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        # Calculate right sum as total minus the current element minus the left sum
        right_sum = total - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1  # Return -1 if no pivot index is found

print(pivot_index(nums))
