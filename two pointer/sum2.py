arr=[-2,10,12,5,1,2,4,5]
target=3


def two_sum(arr,target):
    left=0
    right =len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum == target:
            return[arr[left],arr[right]]
        elif sum<target:
            left+=1
        elif sum>target:
            right-=1
    return None


reslut=two_sum(arr,target)
print(reslut)