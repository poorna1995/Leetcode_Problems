
#o(n)
strs=["Hello", "This","is","poorna"]

def encode(strs):
    res=''
    for s in strs: # for hello in str
        res += str(len(s))+'#'+s
    return res


print(encode(strs))