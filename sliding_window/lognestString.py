s='yyxxwwaw'
# def longest(s):
#     count={}
#     for i in s:
#         if i not in count:
#             count[i]=1
#         else: 
#             count[i]+=1
#     return list(count.values())
# print(longest(s))



def longest(s):
    charSet=set()
    l=0
    result=0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        result=max(result,r-l+1)
    return result

       

