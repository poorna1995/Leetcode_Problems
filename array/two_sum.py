# class solution:
#     def twoSum(self, nums, target):

#         for i in nums:

#             if i in hashset:
#                 return True
#             hashset.add(i)
#             return False


# target = 9
# nums = [2, 7, 11, 15]
# empytset ={}

# for i in enumerate(nums):


# )
# h = target - nums[0]
# if h in empytset:
#     print(empytset[h],i)
# preMap

# print(h)

# if h in nums:
#     print(nums[], h)


# class solution:
#     def twoSum(self, nums, target):
#         emptyset = {}
#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in emptyset:
#                 return (emptyset[diff], i)
#             emptyset[n] = i


# nums = [2, 7, 11, 15, 10, 5]
# target = 9

# print(solution().twoSum(nums, target))
nums=[2,4,12,11,10]
target=13
def twoSum(nums,target):
    for num in nums:
        diff = target - num
        if diff in nums:
            return True
    return False

print(twoSum(nums,target))


def positionTwoSum(nums,target):
    emptySet={}
    for i,num in enumerate(nums):
        diff = target - num
        if diff in emptySet:
            return (emptySet[diff],i)
        emptySet[num] = i
    return 0

print(positionTwoSum(nums,target))

        





























# def twoSum(array):
#     seen = {}
#     for i,n in enumerate(array):
#         diff = target -n

#         if diff in seen:
#             return (seen[diff],i)
#         seen[n] = i