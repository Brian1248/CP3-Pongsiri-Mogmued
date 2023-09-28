menuList = []
priceList = []

def showBill():
    print("---- your Order ----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])

    print('Total:',int(sum(priceList)))


while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()