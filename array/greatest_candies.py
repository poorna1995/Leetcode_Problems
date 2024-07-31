def grtCandies(candies,extra):
`    MaxCandies = max(candies)
    boolen=[]
    for candy in candies:
        total = candy + extra 
        if (total>MaxCandies):
            boolen.append(True)
        else:
            boolen.append(False)
            # return False
    return boolen
`
        






print(grtCandies((6,2,3,2,5,9),5))