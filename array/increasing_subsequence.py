
nums = [1,2,3,4,5]

def increasingTriplet( nums):
    if len(nums) <3:
        return False

    first = float('inf')
    second = float('inf')

    for num in nums:
        if num<=first:
            first = num
        if num <=second:
            second =num
        else:
            return True
    return False


   


        


print(increasingTriplet(nums))

        
