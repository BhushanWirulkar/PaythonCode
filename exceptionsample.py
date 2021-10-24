rate = input("Enter Rate :: ")
Quantity = input("Enter Qty :: ")

try :
    Total = int(rate) * int(Quantity)
    print(Total)
except ValueError :
    print("Invalid value entered")
# This can use if we dont know the exception name
except Exception :
    print("Invalid value entered")