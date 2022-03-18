from random import randrange
def user_enter_a_number():
        #ask the use to enter a # between 1-10:
        # will need to save it
        saved_input = int(input('Enter a number between 0-10:'))
        return saved_input

def random_number():
    return randrange(10)

def values_random_number():
    #saves input from the methods above
    saved_number = user_enter_a_number()
    ran_number = random_number()
    # == means evaluating
    if saved_number == ran_number:
        print('YOU WON THE GAME')
    elif saved_number < ran_number:
        print('To low')
    else:
        print('Too High')
    print(f'You entered:{saved_number}')
    print(f'The random number was:{ran_number}')


values_random_number()


