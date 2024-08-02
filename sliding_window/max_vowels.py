s = "abciiidef"
k = 3

def MaxVowels(s,k):
    vowels ='aeiou'
    current_count=0
    max_count=0
    for i in range (k):
        if s[i] in vowels:
            current_count+=1
    max_count = current_count
    for i in range(k, len(s)):
        if s[i] in vowels:
            current_count += 1
        if s[i - k] in vowels:
            current_count -= 1
        max_count = max(max_count, current_count)

    return max_count
print(MaxVowels(s,k))



def MaxVowels(s, k):
    vowels = 'aeiou'
    max_count = 0
    current_count = 0

    # Initialize the count for the first window
    for i in range(k):
        if s[i] in vowels:
            current_count += 1

    max_count = current_count

    # Slide the window across the string
    for i in range(k, len(s)):
        if s[i] in vowels:
            current_count += 1
        if s[i - k] in vowels:
            current_count -= 1
        max_count = max(max_count, current_count)

    return max_count