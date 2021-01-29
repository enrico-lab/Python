import random
number = random.randint(1,100)

print('guess what number has been chosed by the computer! Pick a number from 1 to 100 included')

guesses = [0]

while True:
    guess = int(input("I am thinking of a number from 1 to 100.\n What's your guess?"))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS!! Try again:')
        continue

    if guess == number:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(number-guess) < abs(number-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(number-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    pass
