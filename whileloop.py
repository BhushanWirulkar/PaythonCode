i = 0

while i <=5:
    print("*"*i)
    i+=1




count=0
isCorrectGuess = False
while count<3:
    colour = input("My favirout colour:: ")
    if(colour.upper()=="BLUE"):
        print("Your guess is correct")
        isCorrectGuess = True
        break
    else:
        print("Wrong Guess")
        count+=1

if(not isCorrectGuess):
    print("Better luck next time!!!!!!!")








