str="5#Hello4#This2#is6#poorna"
def decode(str):
    res,i=[],0
    while i<len(str):
        j=i
        while str[j]!="#":
            j+=1
        length=int(str[i:j])
        print(length)
        res.append(str[j+1:j+1+length])
        i=j+1+length
    return res

print(decode(str))