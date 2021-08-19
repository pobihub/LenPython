xSmall = 0
xLarge =100
for xSmall in range(50):
    xLarge = xLarge + xSmall
    xSmall = xSmall + 10
    print(xLarge, xSmall)
print("xLarge is this big:", xLarge) 
print("xSmall is this small:", xSmall)

lgeStNum = xLarge
smStNum = xSmall

def totalStore(lgPrice, smPrice):
    price1 = lgPrice
    price2 = smPrice
    storeRevenue = xLarge*price1 + xSmall*price2
    return storeRevenue
totalStore(20,10)
print(totalStore(20,10))



