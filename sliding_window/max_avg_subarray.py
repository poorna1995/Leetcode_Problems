nums = [1,12,-5,-6,50,3]
k = 4

# def findMaxAvg(nums,k):
#     max_avg = float('-inf')
#     left =0
#     while left < len(nums):
#         current_total=sum(nums[:k])
#         avg = max(max_avg,current_total//2)
#         left+=1
#         # print(avg)
#         # print(k)
#         # print(current_total)
#     return current_total

# print(findMaxAvg(nums,k))



def findMaxAvg(nums, k):
    if k > len(nums):
        return None  # Or raise an exception, depending on your preference
    
    current_sum = sum(nums[:k])
    max_avg = current_sum / k
    
    for i in range(k, len(nums)):
        print(i)
        current_sum = current_sum - nums[i - k] + nums[i]
        max_avg = max(max_avg, current_sum / k)
    
    return max_avg
print(findMaxAvg(nums,k))