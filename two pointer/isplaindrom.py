# def isPalindrome(str):
#     str=str.lower()
#     print(str)
#     str=''.join (char for char in str if char.isalnum())
#     print(str)
#     return str==str[::-1]

# s="A man, a plan, a canal, Panama!"
# print(isPalindrome(s))




def is_palindrome(str):
    str=str.lower()
    print(str)
    left,right=0,len(str)-1
    while left<right:
        if not str[left].isalnum():
            left+=1
    
            continue
        if not str[right].isalnum():
            right-=1
          
            continue
            
        
        if str[left]!=str[right]:
       
            return False

        left+=1
        right-=1
    return True


s="hello everyone! how are you doing?"
print(is_palindrome(s))

