def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
urprice = int(input("Your Price: "))

print("total:",(vatCalculate((urprice))))

