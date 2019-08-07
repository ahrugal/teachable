answer = "fiskbulle"
tries = 10
disp = ''
for i in answer:
    disp = disp + "_"

display = list(disp)

while tries > 0:
    guess = input("Guess a letter: ")
    if guess in answer:
        print ("Yes, " + guess + " is in the word")
        loc = [pos for pos, char in enumerate(answer) if char == guess]
        for num in loc:
            display[num] = guess
        print (display)
    else:
        print ("No, there is no " + guess + " in the word")
        tries = tries -1
        print ("You have " + str(tries) + " tries left") 

# Comments are fun
