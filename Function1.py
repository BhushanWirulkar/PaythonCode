def greetUser(username,username1):
    print(f'Hello {username} {username1}')

def square(num):
    return num*num
fname = input("Enter your fname : ")
lname = input("Enter your lname : ")
num11 = input("Enter number for square : ")
greetUser(username1=lname,username=fname)
greetUser(fname,username1=lname)
print(square(int(num11)))