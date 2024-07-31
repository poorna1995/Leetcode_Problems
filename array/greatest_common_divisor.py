s = "ABCABC"
t =  "ABC"

# def GCDString(s,t):
#     common=''
#     s[i] == s[j]:
#     append(s[i])
#     i+=1
#     j+=1
#     else:
#         i+=1
#         j+=1


def GCDSting(s,t):
    if s+t !=t+s:
        return ""
    def gcd(a,b):
        print(f'a:{a},b:{b}')
        if len(b) ==0:
            return a
        return gcd(b,a[:len(a)%len(b)])
        # result= gcd(b,a[:len(a)%len(b)])
        print()

    result= gcd(s,t)
    return result
    
    
s = "ABCABC"
t = "ABC"
print(GCDSting(s, t))  # Output: "ABC"


