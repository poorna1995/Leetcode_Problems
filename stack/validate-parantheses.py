# s='([{}})'
# def vaild(s):
#     for i in range(len(s)-1) :
#         if s[:i]== s[:-i]:       
#             return True
#     return False
    

# print(vaild(s))


# s='([{}})'

# def isValid(s):
#     Map={"(":")", "{":"}","[":"]"}
#     stack=[]
#     for c in s:
#         if c not in Map:
#             stack.append(c)
#             continue
#         if not stack or stack[-1]!=Map[c]:
#             return False
#         stack.pop()
#     return not stack


# print(isValid(s))





# s='({[]})'

# Map={"(":")","[":"]","{":"}"}
# stack=[]
# def isValid(s):
#     for c in s:
#         if c not in Map:
#             stack.append(c)
#             print(stack)
#             continue
#         if not stack or stack[-1]!=Map[c]:
#             return False
#         stack.pop()
#     return not stack
        
# print(isValid(s))
# print(stack)
# print(Map)


s='[{(})]'
# def isValid(s):
#     Match={"}":"{","]":"[",")":"("}
#     stack=[]
#     for c in s:
#         if c in Match:
#             if stack and stack[-1] == Match[c]:
#                 stack.pop()
#             else:
#                 return False
#         else:
#             stack.append(c)
#     return True if not stack else False

# print(isValid(s))


    

    



# def isValid(s):
#     Match={"}":"{","]":"[",")":"("}
#     stack=[]
#     for c in s:
#         if c in Match:
#             if stack and stack[-1]== Match[c]:
#                 stack.pop()
#             else:
#                 return False
#         else:
#             stack.append()
#     return True if not stack else False





s='[{})]'

# def valid(S):
#     Match= {"}":"{","]":"[",")":"("}
#     stack=[]
#     for c in s:
#         if c in Match:
#             if stack and stack[-1] == Match[c]:
#                 stack.pop()   
#             else:
#                 return False
#         else:
#             stack.append(c)
#     return True if not stack else False




def isValid(s):
    Match={"}":"{","]":"[",")":"("}
    stack=[]
    for c in s:
        if c in Match:
            if stack and stack[-1] == Match[c]:
                stack.pop()
            else:
                return False   
        else :
            stack.append(c)

    return True if not stack else False

print(isValid(s))




