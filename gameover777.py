import random

# play fair
count = 0
name = input('What is your name? ')
print(
    f'Very good {name} is nice name\nThis game will help you have fun and test your intuition, just guess the number '
    f'from 1 to 30!')
number = random.randint(1, 30)
while count < 8:
    try:
        number1 = int(input('Enter your number: '))
        count += 1
        if number1 > 30:
            print('Your number is over 30')
        if number1 > number:
            print('Your number is more than fictional')
        if number1 < number:
            print('Your number is less than fictional')
        if number1 < 1:
            print('Your number is less than 1')
        if number1 == number:
            print(f'Well done, you guessed my number {number} for {count} attempts')
            break
        if count == 7:
            print('One more try')
    except ValueError:
        print('We need numbers')
else:
    print(f'Unfortunately you did not guess {number}')
input()
