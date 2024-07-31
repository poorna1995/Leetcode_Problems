# #  used to find sub array or string
# prices=[10,1,5,6,7,1] 

# def stock(price):
#     max_num=0
#     left,right=0,len(prices)-1
    

#     while left<right:
#         current_diff= prices[right]-price[left]
#         print(current_diff)
#         max_num=max(current_diff,max_num)
#         print(max_num)
#         if prices[left]<prices[right]:
#             left+=1
#         else:
#             right-=1
#     return max_num


# print(stock(prices))



# def stock(prices):
#     if not prices:
#         return 0
#     min_price=float('inf')
#     max_profit=0

#     for price in prices:
#         if price<min_price:
#             min_price=price
#         current_profit=price-min_price

#         if current_profit>max_profit:
#             max_profit=current_profit
#     return max_profit





def stock(prices):
    if not prices:
        return 0
    
    min_price=float('inf')
    max_profit=0

    for price in prices:
        if price <min_price:
            min_price=price
        print(f"min_price: {min_price}, price: {price}")
        current_profit=price-min_price
        print(f"current price: {current_profit}")


        if current_profit>max_profit:
            max_profit=current_profit
    return max_profit
        


# prices=[10,1,5,6,7,1] 
prices =[7,1,5,3,6,4]
print(stock(prices))


def buyStock(prices):
    max_profit = float('-inf')
    min_price = float('inf')

    for price in prices:
        min_price = min(price,min_price )
        max_profit=max(max_profit, price - min_price )

    return max_profit
print(buyStock(prices))


def butstock(prices):
    buy = prices[0]
    profit =0
    for price in prices:
        if price < buy:
            buy=price
        elif (price-buy) > profit:
            profit = price-buy
    return profit




