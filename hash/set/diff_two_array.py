nums1 = [1,2,3]
nums2 = [2,4,6]

def diff_array(nums1, nums2):
    set1=set(nums1)
    set2=set(nums2)
    print(set1)
    print(set2)
    diff1 = list(set1-set2)
    diff2= list(set2-set1)
    return (diff1, diff2)



# def diff_array(nums1, nums2):
#     return [num for num in nums1 if num not in nums2]

print(diff_array(nums1, nums2))