import random

# for user to guess
def user():
    low=1
    high=random.randint(5,1000)
    attempt=1
    random_num=random.randint(low,high)
    #print("random_num: ",random_num)
    while True:
        guessNum=int(input(f'Guess the number ({low}-{high}): '))
        if (guessNum > random_num):
            print(f'Sorry, guessed number {guessNum} is too high')
            attempt+=1
            #print("attempt: ",attempt)
        elif(guessNum < random_num):
            print(f'Sorry, guessed number {guessNum} is too low')
            attempt+=1
            #print("attempt: ",attempt)
        else:
            if(attempt==1):
                print("You are too good in guessing game \N{slightly smiling face}")
            elif(attempt>10):
                print(f"You have guessed the correct number in {attempt} attempts \N{yawning face}")
            else:
                print(f'Congrats! You have guessed the correct number in {attempt} attempts \N{Face With Party Horn And Party Hat}')   
            break
    YorN=input("Do you want to play again? Y/N ").lower() 
    if(YorN=='y'):
        guess_game()
    if(YorN=='n'):
        exit(0)  

# for computer to gues
def comp(low, high):
    feedback=''
    attempt=1
    while (feedback!='c'):
        if(low!=high):
            guessNum=random.randint(low,high)
        else:
            guessNum=low
        # print('guessNum: ',guessNum)
        feedback=input(f'Is {guessNum} too high(h), too low(l) or correct(c): ').lower()
        if (feedback == 'h'):
            high=guessNum-1
            attempt+=1
        elif(feedback == 'l'):
            low=guessNum+1
            attempt+=1
        else:
            if(attempt==1):
                print("Computer is good in guessing game \N{slightly smiling face}")
            elif(attempt>10):
                print(f"Computer has guessed your number in {attempt} attempts \N{yawning face}")
            else:
                print(f'YaY! The Computer has guessed your number in {attempt} attempts \N{Face With Party Horn And Party Hat}')   
    YorN=input("Do you want to play again? Y/N ").lower() 
    if(YorN=='y'):
        guess_game()
    if(YorN=='n'):
        exit(0)   

# Driver Code
def guess_game():
    choice = input("Enter 'u' if you want to guess number and 'c' if you want computer to guess a number: ").lower()
    if (choice=='u'):
        user()
    elif (choice=='c'):
        low, high = [int(low) for low in input("Enter number between which you want computer to guess the number: ").split()]
        comp(low, high)

guess_game()
