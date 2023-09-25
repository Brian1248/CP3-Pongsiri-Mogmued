def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin1" and passwordInput == "1248":
            showMenu()
    else:
        print("Something wrong, Please try again")
        return login()
def showMenu():
    print("------ Menu ------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()
def menuSelect():
    userSelected = int(input(">"))
    if userSelected == 1:
        print(vatCalculate(totalPrice=(float(input("Price: ")))))
    elif userSelected == 2:
        print(priceCalculate())
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return print("total:",result)
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2),print("vat:7%")


print(login())