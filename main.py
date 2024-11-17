import random
print(
    """
    I am thinking of a 3 digit number (note: the first digit can be 0). Try to guess what it is in 10 guesses.
    Here are some clues:
    What I say:    What it means:
    Pico           One digit is correct but in the wrong position.
    Fermi          One digit is correct and in the correct position.
    Bagel          No digit is correct.
    """
)
firstDigit = "2"#str(random.randint(0,9))
secondDigit = "3"#str(random.randint(0,9))
thirdDigit = "0"#str(random.randint(0,9))

def hintMaker(digit,pos):

    if digit == firstDigit:
        if pos == 1:
            return "Fermi"
        
    elif digit == secondDigit:
        if pos == 2:
            return "Fermi"
    elif digit == thirdDigit:
        if pos == 3:
            return "Fermi"
    else:
        return "Bagels"
    
    return "Pico"
    

numGuesses = 10
guess = None
while numGuesses > 0 and guess != f"{firstDigit}{secondDigit}{thirdDigit}":
    #Get input and make sure its valid
    inputValid = False
    while not inputValid:
        guess = input('Enter your guess (a three digit number).')

        if not guess.isdigit():
            print("Your input is invalid, enter a 3 digit number between 999 and 000")
        else:
            inputValid = True
        
    hint = ""

    for i in range(3):
        hint+= hintMaker(guess[i],i+1)
    
    print(hint)
    

    
