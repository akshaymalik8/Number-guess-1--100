import random

num = random.randint(1,100)
guess = None

while guess != num:
    guess = int(input('Enter the lucky Number between 1 to 100 : '))
    
    if guess>num:
        print('Your guess is bigger then the actual number')

    elif guess<num:
        print('Your guess is smaller then the actual number')    

    
    elif guess == num:
        print('Wow your are genius')
        break

    else:
        print('Opps wrong guess!')