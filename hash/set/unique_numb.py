arr = [1,2,2,1,1,3]
from collections import Counter
def unique(arr):
    count = Counter(arr)
    unique=set()
    print(count)
    for val,counter in count.items():
        if counter in unique:
            return False
        else:
            unique.add(counter)
    return True

        
print(unique(arr))