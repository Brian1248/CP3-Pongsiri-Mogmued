print("----welcome to GPUshop----")
print("******* Please login *******")
username = input("username: ")
password = input("password: ")
if username == "bright" and password == "1248" :
    print("----welcome to GPUshop----")
    print("1. RTX 4070TI : 31000 THB")
    print("2. RTX 4080   : 42800 THB")
    print("3. RTX 4090   : 63500 THB")
    userSelected = int(input("Choose Your Product :   "))

    if userSelected == 1:
       print("1.RTX 4070TI : 31000 THB")
       unit = int(input("How many?  :  "))
       priceProduct = 31000
       total = unit * priceProduct
       print("total :  ",total,"THB")
       print("Thank you for shopping with us")

    elif userSelected == 2:
       print("2.RTX 4080 : 42800 THB")
       unit = int(input("How many? :  "))
       priceProduct = 42800
       total = unit * priceProduct
       print("total :  ",total,"THB")
       print("Thank you for shopping with us")

    elif userSelected == 3:
       print("3.RTX 4090 : 63500 THB")
       unit = int(input("How many? :  "))
       priceProduct = 63500
       total = unit * priceProduct
       print("total :  ",total,"THB")
       print("Thank you for shopping with us")


else: print("error")