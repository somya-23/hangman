from random import randint
from hangman_words import words_list
from hangman_arts import hangmanPics,hangmanLogo

clearConsole=lambda: print('\n'*5)

blank_list = []

def hangmanGame():
    i=randint(0,len(words_list))
    str=words_list[i]

    for b in str:
        blank_list.append('_')

    print(hangmanLogo)
    guessed_list=[]
    steps=0
    while steps<6:
        if '_' not in blank_list:
            print("You Win!")
            break
        a = input("Guess a letter:").lower()
        if a in guessed_list:
            print(f"You have already guessed {a}")
            continue
        else:
            guessed_list.append(a)
        print(f"You guessed {a}.")
        flag=0
        for j in range(0,len(str)):
            if str[j]==a:
                flag=1
                blank_list[j]=a
        if flag==0:
            print("Sorry! that's not in the word, You lose a life")
            steps+=1
        else:
            print("Your guess is correct")
        print(hangmanPics[steps])
        clearConsole()
        print(blank_list)
    if(steps==6):
        print("Opps! you lose all your lifes")

    print(str)
hangmanGame()
