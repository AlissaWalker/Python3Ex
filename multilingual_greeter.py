def greet(name): # functions begin with def; Function is like a method in java
    #name = input("Enter your name:")
    print("Salutations " + name)

def Spanish_greet(name):
    print("Hola " +name)

def French_greet(name):
    print("Bonjour " + name)



# whats in the parenthesis is the argument (parameter in java); this has no argument
def name_input():
    name = input("Enter your name:")
    return name # need () for return if im learning more than 1 thing

def sp_name():
    name = input("Cual es tu nombre?")
    return name

def fr_name():
    name = input("Quel est votre nom?")
    return name
#name_from_user = name_input() # return staements help = a return statement  <--better way
#greet(name_from_user)

# greet(name_input())  #this is another way to get an answer # entire arguments show up as functions

def lanuage_input():
    print("1:English\n" "2:Spanish\n" "3:French")
    pref_language = input("Please select your language with a number")
    if pref_language == '1':
            print("You selected English ")
            greet(name_input())
    elif pref_language == '2':
            print('Has elegido espa')
            Spanish_greet(sp_name())

    elif pref_language == '3':
            print('Vous avez sélectionné')
            French_greet(fr_name())
lanuage_input()