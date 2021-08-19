xSmall = 0
xLarge =100
for xSmall in range(50):
    xLarge = xLarge + xSmall
    xSmall = xSmall + 10
    print(xLarge, xSmall)
print("xLarge is this big:", xLarge) 
print("xSmall is this small:", xSmall)

storeRevenue = 0
def totalStore(xLarge, xSmall):
    storeRevenue = xLarge*10 + xSmall*30
    return storeRevenue
totalStore(1000,200)



