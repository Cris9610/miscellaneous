import random
import time


def Num():
    x = int(input('Pick a number...'))
    return random.randrange(x)


def List():
    y = str(input("Pick something and I'll choose from the list..."))
    return random.choice(y.split())


def DamCuBanu():
    return random.choice(["Heads", 'Tails', 'Between', "Heads", 'Tails'])


def intro():
    try:
        rasp = int(input("Random num(1)"
                         "\nRandom str(2)"
                         "\nToss the coin(3)"
                         "\nExit (4)"
                         "\n Choose what will you do next... "))
        if rasp == 1:
            print(Num())
            input()
            return True
        elif rasp == 2:
            print(List())
            input()
            return True
        elif rasp == 3:
            print('Coin was toss...')
            time.sleep(1)
            print('*Drums*')
            time.sleep(2)
            print('Aaaand...' + " " + DamCuBanu())
            input()
            return True
        elif rasp == 4:
            pass
            return True
        else:
            print('\nUn nr de la 1 la 3. Nu e greu. Hai ca poti\n')
            return False

    except ValueError:
        print('\nAlege un nr. boss...\n')
        return False


while True:
    if intro() is True:
        break

while True:
    z = str(input('Vrei sa mai incerci o data? ( y / n ): ').lower())
    if z == 'y':
        intro()
    elif z == 'n':
        break
    else:
        print('Hai ca nu e greu. Aleg eu ptr tine: "y". Bye Bye.')
        input()
        break
