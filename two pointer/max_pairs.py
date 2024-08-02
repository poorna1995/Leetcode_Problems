nums = [1,2,3,4]
k = 5

def maxPairs(nums,k):
    seen= set()
    count =0
    for num in nums:
        diff = k - num
        if diff in seen:
            count+=1
            seen.remove(diff)
        else:
            seen.add(num)
    return count

print(maxPairs(nums,k))
            

from collections import Counter

def maxPairs(nums,k):
    res, d = 0, Counter(nums)
    print(d)
    for val1, val1_cnt in d.items():
        val2 = k - val1
        print(f'val1:{val1}, val2:{val2}')
        # to get rid of duplicates consider only pairs where val1 >= val2
        if val1 < val2 or val2 not in d: continue 
        res += min(val1_cnt, d[val2]) if val1 != val2 else val1_cnt//2
        
    return res


print(maxPairs(nums,k))
        

