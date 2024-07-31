
def mergeAlternately(word1,word2):
    merged=''
    i,j=0,0
    while i<len(word1) and j<len(word2):
        merged= merged+ word1[i]
        merged= merged+ word2[j]

        i+=1
        j+=1
        #  add remaineind of wordq
    while i<len(word1):
        merged= merged+ word1[i]
        i+=1
    while j<len(word2):
        merged= merged+ word2[j]
        j+=1
    return merged

word1="ab"
word2="pqrs"

print(mergeAlternately(word1,word2))    

