word1 = "abc"
word2 = "bca"
from collections import Counter
def closeness(word1,word2):
    if len(word1)!=len(word2):
        return False
    count1 = Counter(word1)
    count2 = Counter(word2)
    print(count1,count2)
    # Check if the sets of characters are the same
    if set(count1.keys()) != set(count2.keys()):
        return False
    print(count1.keys())
    print(count2.keys())
    # Check if the sorted frequencies are the same
    if sorted(count1.values()) != sorted(count2.values()):
        return False
    print(count1.values())
    
    return True

print(closeness(word1,word2))