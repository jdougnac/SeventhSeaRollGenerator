import random


def explode(academy):
    lista = []
    number = 10
    if academy == False:
        while number == 10:
            lista.append(number)
            number = random.randint(1,10)#1,11)
            if number !=10:            
                lista.append(number)
    elif academy == True:
        while number == 9 or number == 10:
            lista.append(number)
            number = random.randint(1,10)#1,11)
            if number !=10 and number != 9:            
                lista.append(number)
    return lista
    return lista

def reroll_die(explode, academy):
    die= random.randint(1,10)
    if die == 10 and explode == True :
        die = explode(academy)
    elif die == 9 and explode == True and academy == True:
        die = explode(academy)
    return die
    



#reroll without choice
def reroll_ones():
    die = random.randint(2,10)

    return die

#reroll where you can choose; the higher dice will always be picked
def reroll_pick(number):
    die= random.randint(1,10)
    if number > die:
        return number
    else:
        return die        

def roll(amount, explodes, reroll_ones, legendary_attribute, academy):
    roll =[]
    for dice in range(0,amount):
        if reroll_ones == False:
            result = random.randint(1,10)
        else:
            result = random.randint(2,10)
        if explodes == True and result == 10:
            extra = explode(False)
            for item in extra:
                roll.append(item)
            
        elif explodes == True and result == 9 and academy == True:
            extra = explode(True)
            for item in extra:
                roll.append(item)
        else:
            roll.append(result)
    roll.sort()                                                         
    return roll



