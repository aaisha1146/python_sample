winning_no=10
guessed_no=input("guess any number between 1 to 20 ")
guessed_no=int(guessed_no)
if guessed_no==winning_no:
    print("YOU WIN!!!!")
else:
    if guessed_no<10:
        print("too low")
    else:
        print("too high")
