print("Please think of a number between 0 and 100!")

low = 0
high = 100
num = 50
promtt = "Is your secret number {}?\nEnter 'h' to indicate \
the guess is too high. Enter 'l' to indicate the guess is too low. Enter\
 'c' to indicate I guessed correctly."

answer = input(promtt.format(num))
while answer != "c":
    if answer not in ["h", "l"]:
        print("Sorry, I did not understand your input.")
        answer = input(promtt.format(num))
    elif answer == "l":
        low = num
        num = ((low + high)//2)
        answer = input(promtt.format(num))
    else:
        high = num
        num = ((low + high)//2)
        answer = input(promtt.format(num))
print("Game over. Your secret number was: {}".format(num))



