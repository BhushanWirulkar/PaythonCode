num = input("Please Enter your phone number : ")
dict1 = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "four",
    5 : "Five",
    6 : "😍",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine",
    0 : "Zero"
}


number = "";

for num1 in num:
    number+=dict1[int(num1)]+" "


print(dict1.get(11),"Nahi ahe re item")
print(number)


