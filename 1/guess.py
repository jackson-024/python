import  random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while (guess != random_number):
        guess = int(input(f'guess a number between 1 and {x}: '))
        
        if guess < random_number:
            print('Sorry. Too Low!')
        elif guess >random_number:
            print('Sorry. Too high!')

    print(f'Yaaay you got it \
         {random_number} is the random number')
            
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high) 
        else:
            guess = low
            
        feedback = input(f'is {guess} to high(H), too low(L) , or correct(C)').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The coputer guessed your nummber, {guess}, correctly')


computer_guess(10) 
    