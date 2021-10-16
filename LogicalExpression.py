age = input("Please enter your age :: ")
criminal_record = True


if(int(age) > 18 and not criminal_record):
    print("You are eligible for Passport")
else:
    if (criminal_record):
        print("You have criminal record")
    print("You are not eligible for Passport")