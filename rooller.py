import random


#def explode(academy):
def explode(addToEachDie, amount = 0):
    lista = []
    number = 10
    if amount > 10: #
        number = amount #
    if addToEachDie == 0:
        while number >= 10: ## ==10
            lista.append(number)
            number = random.randint(1,10)
            if number !=10:            
                lista.append(number)
    elif addToEachDie != 0:
        while number >= 10-addToEachDie:
            lista.append(number)
            number = random.randint(1,10)
            if number < 10-addToEachDie:            
                lista.append(number)
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

#def roll(amount, explodes, reroll_ones, academy):
def roll(amount, explodes, reroll_ones, addToEachDie):
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
            
        #elif explodes == True and result == 9 and academy == True:
        elif explodes == True and result == 10-addToEachDie and addToEachDie != 0:
            #extra = explode(True)
            extra = explode(addToEachDie)
            for item in extra:
                roll.append(item)
        else:
            roll.append(result)
    roll.sort()                                                         
    return roll



