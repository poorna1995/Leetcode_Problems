# def kElement(nums,k):
#     count={}
#     freq=[[] for i in range(len)+1 ]
#     for n in nums:
#         count[n]=1+count.get(n,0)
#     for n,c in count.items():
#         freq[c].append(n)
#     res=[]
#     for i in range (len(freq)-1,0,-1):
#         for n in freq[i]:
#             res.append(n)
#             if len(res)==k:
#                 return res
   
      

            

# def topK(nums,k):
#     count={}
#     freq=[[] for i in range(len(nums)+1)] # freq=[[].[].[],[],[],[],[]]
#     for n in nums:
#         count[n] = 1+count.get(n,0) # count[1]= 1+count.get(1,0) -check the numbe is in count ., 1 is not there in count
#     for n,c in count.items():
#         freq[c].append(n)
#     res=[]
#     for i in range (len(freq)-1,0,-1):
#         for n in freq[i]:
#             res.append(n)
#             if len(res)==k


# def top(nums,k):
#     count={}
#     freq=[[] for i in range(len(nums)+1)]
#     for n in nums:
#         count[n]= 1+count.get(n,0)
#     for n,c in count.items():
#         freq[c].append(n)
#     res=[]
#     for i in range(len(freq) -1,0,-1):
#         for n in freq[i]:
#             res.append(n)
#             if len(res)==k:
#                 return res
        

# print(top([1,1,1,1,3,4,12],3))



# nums= [1,1,1,1,3,4,12]
# k=2

# def topK(nums,k):
#     count={}
#     freq=[[] for i in range(len(nums)+1)]
#     for n in nums:
#         count[n]= 1+count.get(n,0)
#     for n,c in count.items():
#         freq[c].append(n)
#     res=[]
#     for i in range(len(freq)-1,0,1):
#         for n in freq[i]:
#             res.append(n)
#             if len(res)==k:
#                 return res



    

nums= [1,1,1,1,3,3,4,12]
k=2

from collections import Counter
import heapq

# def topK(nums,k):
#     n= len(nums)
#     counter = Counter(nums)
#     bucket = [0]*(n+1)
#     # print(counter)

#     for num,freq in counter.items():
#         if bucket[freq] == 0:
#             bucket[freq] ==[num]
#         else:
#             bucket[freq].append(num)
#     ret=[]
#     for i in range(n,0,-1):
#         if bucket[i]!=0:
#             ret.extend(bucket[i])
#         if len(ret) ==k:
#             return ret

# print(topK(nums,k))


def topk(nums,k):
    counter =Counter(nums)
    heap = []

    for num,freq in counter.items():
        if len(heap) < k:
            heapq.heappush(heap,(freq,num))
        else:
            heapq.heappushpop(heap,(freq,num))
    return [t[1] for t in heap]

print(topk(nums,k))




