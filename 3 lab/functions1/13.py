from  random import randint

def guessTheNum(str1):
    q = False
    cnt = 1
    n = randint(1, 20)

    while q == False:
        print("Take a guess.")
        n1 = int(input())
        if n == n1:
            print(f"Good job, {str1}! You guessed my number in {cnt} guesses!")
            break
        else:
            cnt += 1
            if n1 > n:
                print ("Your guess is too high.")
            else:
                print("Your guess is too low.")

str1 = input("Hello! What is your name?\n")

print(f"Well, {str1}, I am thinking of a number between 1 and 20.")

s = guessTheNum(str1)