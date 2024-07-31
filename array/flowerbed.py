def placeFlower(flowerbed,n):
    count =0
    for i in range(0,len(flowerbed)):
        if flowerbed[i] == 0:
            if (i=0 or flowerbed[i-1]==0) and (flowerbed[i+1] or i == len(flowerbed)-1):
                flowerbed[i]=1
                count+=1
                if (count>=n):
                    return True
    return count>=n
                


