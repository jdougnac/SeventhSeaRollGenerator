from tkinter import *
import iiterator
import rooller
root = Tk()


result= [] 
pending_rerolls=0
reroll_lowest = False
reroll_many = False
petty_luck = False
mythic = False
greater_luck = False

def roll_dice():
    global result 
    global pending_rerolls
    global reroll_lowest
    global reroll_many
    global petty_luck
    global greater_luck
    global mythic
    pending_rerolls = 0    
    rerollOneYesBTN.configure(state='disabled')
    rerollOneNoBTN.configure(state='disabled')

    rerollSomeTXT.configure(state='disabled')
    rerollSomeBTN.configure(state='disabled')
    
    if explotanVar.get() == 1:
        explode = True
    else:
        explode = False      
    addToEachDie = addToEachDieVar.get()
    if legTraitVar.get() == 1:
        legendary_trait = True
    else:
        legendary_trait = False

    try:
        target_number = int(dificultadTXT.get())
        if target_number <10:
            dificultadTXT.delete(0, END)
            dificultadTXT.insert(0, '10')
            return
    except ValueError:
        dificultadTXT.delete(0, END)
        dificultadTXT.insert(0, '10')
        return        
    try:
        dice_amount = int(dadosTXT.get())
        if dice_amount <=0:
            dadosTXT.delete(0, END)
            return
    except ValueError:
        dadosTXT.delete(0, END)
        return
    if legendary_trait == True:
        dice_amount -=1        
    result=rooller.roll(dice_amount,explode, False, int(addToEachDie))
    if madLuckTXT.get() != '':
        dados_extra = madLuckTXT.get().split()
        for element in dados_extra:
            try:
                if int(element) >0 and int (element)<11:
                    result.append(int(element))
                else:
                    resultTXT.delete('1.0', END)
                    madLuckTXT.delete(0, END)
                    return
            except ValueError:
                resultTXT.delete('1.0', END)
                madLuckTXT.delete(0, END)
                return
            result.sort()
    if legendary_trait == True:             
        if explode == True:
            extra = rooller.explode(int(addToEachDie))
            for item in extra:
                result.append(item)
        else:
            result.append(10)
        result.sort()
    madLuckTXT.delete(0, END)   
    if dadoMasBajoVar.get() ==1:
        reroll_lowest = True
        pending_rerolls +=1
        rerollOneYesBTN.configure(state='normal')
        rerollOneNoBTN.configure(state='normal')
    if pettyLuckVar.get() != '0':
        petty_luck = True
        pending_rerolls +=1
        pettyLuckYesBTN.configure(state='normal')
        pettyLuckNoBTN.configure(state='normal')
    if greaterLuckVar.get() != '0':
        greater_luck = True
        pending_rerolls +=1        
        greaterLuckBTN.configure(state='normal')
        greaterLuckTXT.configure(state='normal')
    if rerollManyVar.get() == 1:
        reroll_many = True
        pending_rerolls +=1
        rerollSomeTXT.configure(state='normal') 
        rerollSomeBTN.configure(state='normal')
    if mythicCheckVar.get() == 1:
        mythic = True
        pending_rerolls +=1
        mythicMenu.configure(state='normal') 
        mythicBTN.configure(state='normal')        
    if reroll_lowest == False and reroll_many == False and petty_luck == False and mythic == False and greater_luck == False:
        show_results()
    else:
        resultTXT.delete('1.0', END)
        resultTXT.insert(INSERT,f'Roll:\n{result}.\n')

def reroll_dice(roll, amount, category):
    global result 
    global pending_rerolls
    global reroll_lowest
    global reroll_many
    if category == 'reroll_many':
        try:
            amount = int(rerollSomeTXT.get())
            if amount <0 or amount > len(roll):
                rerollSomeTXT.delete(0, END)
                return
        except ValueError:
            rerollSomeTXT.delete(0, END)
            return
    elif category == 'mythic': ###
        amount = int(mythicVar.get())
        if amount > len(roll):
            mythicVar.set('0')
            return
    pending_rerolls -=1
    if explotanVar.get() == 1:
        explode = True
    else:
        explode = False
    addToEachDie = addToEachDieVar.get()
    print('zzz', result)
    print('ddd', result[0])
    for element in range(0, amount):
        first_die = result[0]
        del result[0]        
        dado = rooller.roll(1, explode, False, int(addToEachDie))
        if category == 'mythic' and first_die > dado[0]:
            result.append(first_die)
        else:
            for item in dado:
                result.append(item)
    result.sort()
    
    if category == 'reroll_one':
        rerollOneYesBTN.configure(state='disabled')
        rerollOneNoBTN.configure(state='disabled')
        reroll_lowest = False 
    elif category == 'reroll_many':
        rerollSomeTXT.configure(state='disabled')
        rerollSomeBTN.configure(state='disabled')
        reroll_many = False
    elif category == 'mythic':
        mythicVar.set('0')
        mythicMenu.configure(state='disabled')
        mythicBTN.configure(state='disabled')
        mythic = False        
    
    if pending_rerolls == 0:        
        show_results()
    else: 
        resultTXT.delete('1.0', END)
        resultTXT.insert(INSERT,f'Roll:\n{result}.\n')


def use_petty_luck(roll, yes_no):
    global result 
    global petty_luck
    global pending_rerolls

    pending_rerolls -=1
  

    if explotanVar.get() == 1:
        explode = True
    else:
        explode = False    
    if yes_no == True:    
        new_dice = int(pettyLuckVar.get())+1
        del result[0]        
        if explode == True and new_dice >= 10- int(addToEachDieVar.get()):
            extra = rooller.explode(int(addToEachDieVar.get()))
            for item in extra:
                result.append(item)        
            
        result.append(new_dice)
        result.sort()

    pettyLuckYesBTN.configure(state='disabled')
    pettyLuckNoBTN.configure(state='disabled')
    petty_luck = False 
    pettyLuckVar.set('0')
    if pending_rerolls == 0:        
        show_results()
    else: 
        resultTXT.delete('1.0', END)
        resultTXT.insert(INSERT,f'Roll:\n{result}.\n')

def use_greater_luck():
    global result
    global pending_rerolls
    global greater_luck
    addToEachDie = addToEachDieVar.get()
   
    try:
        position = int(greaterLuckTXT.get())
        if position <0 or position > len(result):
            greaterLuckTXT.delete(0, END)
            return
    except ValueError:
        greaterLuckTXT.delete(0, END)
        return
    pending_rerolls -=1
    if position==0:
        show_results()
    else:
        altered_dice = result[position-1]+ int(greaterLuckVar.get())
        del result[position-1]
        if altered_dice >= 10- int(addToEachDieVar.get()):
            extra = rooller.explode(int(addToEachDieVar.get()), altered_dice)
            for item in extra:
                result.append(item)          
        
        else:
            result.append(altered_dice)
        
        result.sort()

    greaterLuckBTN.configure(state='disabled')    
    greater_luck = False 
    greaterLuckVar.set('0')###
    if pending_rerolls == 0:        
        show_results()
    else: 
        resultTXT.delete('1.0', END)
        resultTXT.insert(INSERT,f'Roll:\n{result}.\n')        
        
    
def show_results(original_list=[]):
    global result
    global reroll_lowest
    global reroll_many
    
    dice = dadosTXT.get()
    iiterator.exitos = []
    original_roll = result.copy()
    iiterator.roll_list = result
    
    iiterator.target_number = int(dificultadTXT.get())



    if int(addToEachDieVar.get()) !=0:
        for x in range(0,len(result)):
            result[x]=result[x]+int(addToEachDieVar.get())
            
    iiterator.target_number = int(dificultadTXT.get())

    result = iiterator.start_iterating()

    if reroll_lowest == False and reroll_many == False:
        roll_show = []
        for element in result[0]:
            for x in element:
                roll_show.append(x)
        for element in result[1]:
            roll_show.append(element)
        roll_show.sort()
        skillRango4 = skillRango4Var.get()
        if skillRango4 == 0:
            full_list = result[0]+result[1]
            resultTXT.delete('1.0', END)
            resultTXT.insert(INSERT,f'Dice amount: {dice}.\nTarget Number: {dificultadTXT.get()}.\nRoll: \n{roll_show}\nRaises:\n{result[0]}\nRaises:\n{len(result[0])} \nRemaining Dice: \n{result[1]}\n')
        elif skillRango4 == 1:            
            iiterator.exitos =[]            
            iiterator.roll_list = roll_show
            roll_to_print = roll_show.copy()
            iiterator.target_number = int(dificultadTXT.get())+5
            result_list2 = iiterator.start_iterating()
            dados_sobrantes = result[1].copy()                
            resultTXT.delete('1.0', END)
            resultTXT.insert(INSERT,f'Dice Amount: {dice}.\n')
            numeroObjetivoDosExitos = str(int(dificultadTXT.get())+5)
            resultTXT.insert(END,f'Target Number for 2 Raises: {numeroObjetivoDosExitos}.\nRoll:\n{roll_to_print}\nSets of 2 Raises:\n{result_list2[0]}\n')
            iiterator.exitos =[]            
            iiterator.roll_list = result_list2[1]
            iiterator.target_number = int(dificultadTXT.get())
            result_list3 = iiterator.start_iterating()            
            resultTXT.insert(END,f'Sets of one Raise:\n{result_list3[0]}\nRemaining Dice:\n{result_list3[1]}\nTotal Raises:\n{str(len(result_list2[0]*2)+len(result_list3[0]))} \n')
    else:
        resultTXT.delete('1.0', END)
        resultTXT.insert(INSERT,f'Amount of dice: {dice}.\nRoll: \n{result[0]}\n')
    addToEachDieVar.set('0')#
    rerollOneYesBTN.configure(state='disabled') 
    rerollOneNoBTN.configure(state='disabled') 
    rerollSomeTXT.configure(state='disabled') 
    rerollSomeBTN.configure(state='disabled') 


def reset():
    global result 
    global pending_rerolls
    global reroll_lowest
    global reroll_many
    global petty_luck
    global greater_luck
    global mythic
    pending_rerolls=0
    reroll_lowest = False
    reroll_many = False
    petty_luck = False
    mythic = False
    greater_luck = False
    result=[]
    resultTXT.delete('1.0', END)
    dificultadTXT.delete(0, END)
    madLuckTXT.delete(0, END)
    dificultadTXT.insert(0, '10')
    dadosTXT.delete(0, END)
    rerollOneYesBTN.configure(state='disabled')
    rerollOneNoBTN.configure(state='disabled')
    pettyLuckYesBTN.configure(state='disabled')
    pettyLuckNoBTN.configure(state='disabled')
    greaterLuckBTN.configure(state='disabled')
    greaterLuckTXT.configure(state='disabled')
    rerollSomeTXT.configure(state='disabled') 
    rerollSomeBTN.configure(state='disabled')
    mythicMenu.configure(state='disabled') 
    mythicBTN.configure(state='disabled') 
    mythicVar.set('0')
    addToEachDieVar.set('0')
    greaterLuckVar.set('0')
    pettyLuckVar.set('0')
    explotanCheck.deselect()
    dadoMasBajoCheck.deselect()
    skillRango4Check.deselect()
    mythicCheck.deselect()
    rerollManyCheck.deselect()
    legTraitCheck.deselect()
    explotanCheck.deselect()



dadosLab=Label(root, text ="Dice: ")
dadosTXT=Entry(root, width =5)
#dadosTXT.insert(0,"10")

dificultadLab=Label(root, text ="Difficulty: ")
dificultadTXT=Entry(root, width =5)
dificultadTXT.insert(0,"10")

explotanLab=Label(root, text ="10s explode")
explotanVar = IntVar()
explotanCheck=Checkbutton(root, width = 15, variable = explotanVar)

dadoMasBajoLab=Label(root, text ="Reroll one die")
dadoMasBajoVar = IntVar()
dadoMasBajoCheck=Checkbutton(root, width = 15, variable = dadoMasBajoVar)

skillRango4Lab=Label(root, text ="Skill rank 4")
skillRango4Var = IntVar()
skillRango4Check=Checkbutton(root, width = 15, variable = skillRango4Var)

#academyLab=Label(root, text ="+1 to each die")
#academyVar = IntVar()
#academyCheck=Checkbutton(root, width = 15, variable = academyVar)

addToEachDieLab = Label(root, text = "Add to each die")
addToEachDieVar = StringVar(root)
addToEachDieChoices = ['0','1','2','3','4','5','6']
addToEachDieVar.set('0')
addToEachDieMenu = OptionMenu(root, addToEachDieVar, *addToEachDieChoices)

pettyLuckLab = Label(root, text = "Petty Luck Ranks")
pettyLuckVar = StringVar(root)
pettyLuckChoices = ['0','1','2','3','4','5']
pettyLuckVar.set('0')
pettyLuckMenu = OptionMenu(root, pettyLuckVar, *pettyLuckChoices)


greaterLuckLab = Label(root, text = "Greater Luck Ranks")
greaterLuckVar = StringVar(root)
greaterLuckChoices = ['0','1','2','3','4','5']
greaterLuckVar.set('0')
greaterLuckMenu = OptionMenu(root, greaterLuckVar, *greaterLuckChoices)
useGreaterLuckLab = Label(root, text = "Die position for Greater Luck")
greaterLuckTXT=Entry(root, width =5)
greaterLuckTXT.configure(state = 'disabled')
greaterLuckBTN=Button(root, text ='Use Greater Luck', state = 'disable', command = lambda: use_greater_luck())


mythicVar = StringVar(root)
mythicChoices = ['0','1','2','3','4','5']
mythicVar.set('0')
mythicMenu = OptionMenu(root, mythicVar, *mythicChoices)
mythicBTN=Button(root, text ='Mythic Reroll', state = 'disable', command = lambda: reroll_dice(result, 0, 'mythic'))
mythicMenu.configure(state="disabled")

mythicLab=Label(root, text ="Has Mythic?")
mythicCheckVar = IntVar()
mythicCheck=Checkbutton(root, width = 15, variable = mythicCheckVar)

rerollManyLab=Label(root, text ="Devil's Luck")
rerollManyVar = IntVar()
rerollManyCheck=Checkbutton(root, width = 15, variable = rerollManyVar)

legTraitLab=Label(root, text ="Legendary Trait")
legTraitVar = IntVar()
legTraitCheck=Checkbutton(root, width = 15, variable = legTraitVar)

rollBTN=Button(root, text ='Roll!', command = roll_dice)
resetBTN=Button(root, text ='Reset', command = reset)

resultLab = Label(root, text = "Results:")
resultTXT = Text (root, height = 15, width = 40)

rerollOneLab=Label(root, text ="Reroll lowest die?")
rerollOneYesBTN=Button(root, text ='Yes', state = 'disable', command = lambda: reroll_dice(result, 1, 'reroll_one'))
rerollOneNoBTN=Button(root, text ='No', state = 'disable', command = lambda: reroll_dice(result, 0, 'reroll_one'))

pettyLuckLab=Label(root, text ="Petty Luck:")
usePettyLuckLab=Label(root, text ="Use Petty Luck?")
pettyLuckYesBTN=Button(root, text ='Yes', state = 'disable', command = lambda: use_petty_luck(result, True)) ##
pettyLuckNoBTN=Button(root, text ='No', state = 'disable', command = lambda: use_petty_luck(result, False)) ##


rerollSomeLab=Label(root, text ="Dice to reroll:")
rerollSomeTXT=Entry(root, state = 'disable')
rerollSomeBTN=Button(root, text ='Reroll', state = 'disable', command = lambda: reroll_dice(result, rerollSomeTXT.get(), 'reroll_many'))

madLuckLab = Label(root, text ="Mad Luck Dice: ")
madLuckTXT = Entry(root, width =20)

dadosLab.grid(row=0, column = 0)
dadosTXT.grid(row=0, column = 1)

dificultadLab.grid(row=0, column = 2)
dificultadTXT.grid(row=0, column = 3)

explotanLab.grid(row=1, column = 0)
explotanCheck.grid(row=1, column= 1)

dadoMasBajoLab.grid(row=2, column = 0)
dadoMasBajoCheck.grid(row=2, column= 1)

skillRango4Lab.grid(row=3, column = 0)
skillRango4Check.grid(row=3, column= 1)

rerollOneLab.grid(row=1, column = 2)
rerollOneYesBTN.grid(row=2, column = 2)
rerollOneNoBTN.grid(row=3, column = 2)

rerollSomeLab.grid(row=4, column = 2)
rerollSomeTXT.grid(row=5, column = 2)
rerollSomeBTN.grid(row=6, column = 2)


addToEachDieLab.grid(row=4, column = 0)
addToEachDieMenu.grid(row=4, column = 1)

rerollManyLab.grid(row=5, column = 0)
rerollManyCheck.grid(row=5, column = 1)

legTraitLab.grid(row=6, column = 0)
legTraitCheck.grid(row=6, column = 1)

rollBTN.grid(row=8, column = 0)
resetBTN.grid(row=8, column = 1)

resultLab.grid(row=9, column = 0)
resultTXT.grid(row=10, column = 0)

pettyLuckLab.grid(row=0, column = 4)
pettyLuckMenu.grid(row=0, column = 5)

usePettyLuckLab.grid(row=1, column = 4)
pettyLuckYesBTN.grid(row=2, column = 4)
pettyLuckNoBTN.grid(row=3, column = 4)


mythicLab.grid(row=4, column = 4)
mythicCheck.grid(row=4, column = 5)

mythicMenu.grid(row=5, column = 4)
mythicBTN.grid(row=6, column = 4)

madLuckLab.grid(row=7, column = 4)
madLuckTXT.grid(row=8, column = 4)

greaterLuckLab.grid(row=0, column = 6)
greaterLuckMenu.grid(row=1, column = 6)
useGreaterLuckLab.grid(row=2, column = 6)
greaterLuckTXT.grid(row=3, column = 6)
greaterLuckBTN.grid(row=4, column = 6)





root.mainloop()



