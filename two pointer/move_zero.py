nums = [0,1,0,3,12]
def MoveZero(nums):
    l=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[l] =nums[i]
            l+=1
    for i in range(l,len(nums)):
        nums[i]=0
    return nums



print(MoveZero(nums))