s= "the sky is   blue"

def mergeWords(s):
    string = s.split( )
    print(string)
    l,r= 0,len(string)-1
    while l<r:
        string[l],string[r] = string[r], string[l]
        l+=1
        r-=1
    return ' '.join(string)


print(mergeWords(s))


# def removeExtraSpaces(s):
#     # Use the replace method to replace multiple spaces with a single space
#     while "  " in s:
#         s = s.replace("  ", " ")
#     # Strip leading and trailing spaces
#     s = s.strip()
#     string = s.split(' ')
#     print(string)
#     l,r= 0,len(string)-1
#     while l<r:
#         string[l],string[r] = string[r], string[l]
#         l+=1
#         r-=1
#     return ' '.join(string)



# print(removeExtraSpaces(s))




# def ShortremoveExtraSpaces(s):
#     print(s.split())
#     return " ".join(s.split()[::-1])

# print(ShortremoveExtraSpaces(s))


