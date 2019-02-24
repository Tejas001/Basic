import random
print("Hello what is your name?")
name = input()

print("Your name is " + name + " please guess number between 1 to 10")
secret = random.randint(1,10)

for guesstaken in range(1,10):
    print("Guess no.")
    guess = int(input())

    if guess < secret:
        print("Guess is low")
    elif guess > secret:
        print("Guess is high")
    else:
        break

if guess == secret:
    print("Good Job"+name+'!')
else:
    print("The secret no is"+str(secret)+'Thank you')

