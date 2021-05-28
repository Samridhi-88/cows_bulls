import random

digit = 5
name = input("enter your name=")
print("welcome",name,"in this gurssing game!!!!")
def getSecretNum():
    number = list(range(10))
    random.shuffle(number)
    return number

def getclues():
    numbers = getSecretNum()
    secret_num = []
    for i in range(digit):
        secret_num.append(numbers[i])
    return secret_num

def game():
    bull=[]
    cow=[]
    num = getclues()
    print(num)
    i=0
    guess=10
    while guess>0:
        guess_num=int(input("enter the guess"))
        position=int(input("enter the position"))
        print("****(*_*)****")
        if guess_num in num:
            index=num.index(guess_num)
            if index==position:
                if guess_num not in bull:
                   bull.insert(index,guess_num)
                   print("bull",bull)
                else:
                    print("you used this digit try any different")
            else:
                cow.append(guess_num)
                print("this number is in the list you can reuse it ",cow)
        if bull==num:
            print("congractulation you win*")
            break
        guess-=1
        print(guess,"turn are left")
    else:
        print("you loose the game")
    return bull

def play_again():

    while True:
        again=input("you want to play again yes or no ")
        if again=="yes":
            game()
        else:
            break
play_again()

        