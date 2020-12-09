from tkinter import *
import iiterator
import rooller
root = Tk()


result= [] 
pending_rerolls=0
reroll_lowest = False
reroll_many = False

def roll_dice():
    global result 
    global pending_rerolls
    global reroll_lowest
    global reroll_many

    pending_rerolls = 0    
    rerollOneYesBTN.configure(state='disabled')
    rerollOneNoBTN.configure(state='disabled')

    rerollSomeTXT.configure(state='disabled')
    rerollSomeBTN.configure(state='disabled')
    if explotanVar.get() == 1:
        explode = True
    else:
        explode = False      
    if academyVar.get() == 1:
        academy = True
    else:
        academy = False       
    result=rooller.roll(int(dadosTXT.get()),explode, False, False, academy)
    if dadoMasBajoVar.get() ==1:
        reroll_lowest = True
        pending_rerolls +=1
        rerollOneYesBTN.configure(state='normal')
        rerollOneNoBTN.configure(state='normal')
    if rerollManyVar.get() == 1:
        reroll_many = True
        pending_rerolls +=1
        rerollSomeTXT.configure(state='normal') 
        rerollSomeBTN.configure(state='normal') 
    if reroll_lowest == False and reroll_many == False:
        show_results()
    else:
        resultTXT.delete('1.0', END)
        resultTXT.insert(INSERT,f'Roll:\n')
        resultTXT.insert(INSERT,f'{result}.\n')

def reroll_dice(roll, amount, category):
    global result 
    global pending_rerolls
    global reroll_lowest
    global reroll_many    
    pending_rerolls -=1
    if explotanVar.get() == 1:
        explode = True
    else:
        explode = False      
    if academyVar.get() == 1:
        academy = True
    else:
        academy = False
    for element in range(0, amount):
        del result[0]
        dado = rooller.roll(1, explode, False, False, academy)
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
    if pending_rerolls == 0:        
        show_results()
    else: 
        resultTXT.delete('1.0', END)
        resultTXT.insert(INSERT,f'Roll:\n')
        resultTXT.insert(INSERT,f'{result}.\n')
    
def show_results(original_list=[]):
    global result
    global reroll_lowest
    global reroll_many
    
    dice = dadosTXT.get()
    iiterator.exitos = []
    original_roll = result.copy()
    iiterator.roll_list = result
    
    iiterator.target_number = int(dificultadTXT.get())


    if academyVar.get() == 1:
        for x in range(0,len(result)):
            result[x]=result[x]+1
                
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
            resultTXT.insert(INSERT,f'Dice amount: {dice}.\n')
            resultTXT.insert(END,f'Target Number: {dificultadTXT.get()}.\n')
            resultTXT.insert(END,'Roll: \n')
            resultTXT.insert(END,f'{roll_show}\n')
            resultTXT.insert(END,'Raises: \n')    
            resultTXT.insert(END,f'{result[0]}\n')
            resultTXT.insert(END,f'Raises:\n{len(result[0])} \n')
            resultTXT.insert(END,'Reamining Dice: \n')
            resultTXT.insert(END,f'{result[1]}\n')
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
            resultTXT.insert(END,f'Target Number for 2 Raises: {numeroObjetivoDosExitos}.\n')
            resultTXT.insert(END,'Roll: \n')
            resultTXT.insert(END,f'{roll_to_print}\n')
            resultTXT.insert(END,'Sets of 2 Raises: \n')    
            resultTXT.insert(END,f'{result_list2[0]}\n')
            iiterator.exitos =[]            
            iiterator.roll_list = result_list2[1]
            iiterator.target_number = int(dificultadTXT.get())
            result_list3 = iiterator.start_iterating()            
            resultTXT.insert(END,f'Sets of one Raise:\n')
            resultTXT.insert(END,f'{result_list3[0]}\n')
            resultTXT.insert(END,f'Remaining Dice:\n')
            resultTXT.insert(END,f'{result_list3[1]}\n')            
            resultTXT.insert(END,f'Total Raises:\n')        
            resultTXT.insert(END,f'{str(len(result_list2[0]*2)+len(result_list3[0]))} \n')
    else:
        resultTXT.delete('1.0', END)
        resultTXT.insert(INSERT,f'Amount of dice: {dice}.\n')        
        resultTXT.insert(END,'Roll: \n')
        resultTXT.insert(END,f'{result[0]}\n')
    rerollOneYesBTN.configure(state='disabled') 
    rerollOneNoBTN.configure(state='disabled') 
    rerollSomeTXT.configure(state='disabled') 
    rerollSomeBTN.configure(state='disabled') 





dadosLab=Label(root, text ="Dice: ")
dadosTXT=Entry(root, width =5)
dadosTXT.insert(0,"10")

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

academyLab=Label(root, text ="+1 to each die")
academyVar = IntVar()
academyCheck=Checkbutton(root, width = 15, variable = academyVar)

rerollManyLab=Label(root, text ="Devil's Luck")
rerollManyVar = IntVar()
rerollManyCheck=Checkbutton(root, width = 15, variable = rerollManyVar)

rollBTN=Button(root, text ='Roll!', command = roll_dice)

resultLab = Label(root, text = "Results:")
resultTXT = Text (root, height = 15, width = 40)

rerollOneLab=Label(root, text ="Reroll lowest die?")
rerollOneYesBTN=Button(root, text ='Yes', state = 'disable', command = lambda: reroll_dice(result, 1, 'reroll_one'))
rerollOneNoBTN=Button(root, text ='No', state = 'disable')

rerollSomeLab=Label(root, text ="Dice to reroll:")
rerollSomeTXT=Entry(root, state = 'disable')
rerollSomeBTN=Button(root, text ='Reroll', state = 'disable', command = lambda: reroll_dice(result, int(rerollSomeTXT.get()), 'reroll_many'))


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


academyLab.grid(row=4, column = 0)
academyCheck.grid(row=4, column = 1)

rerollManyLab.grid(row=5, column = 0)
rerollManyCheck.grid(row=5, column = 1)

rollBTN.grid(row=6, column = 0)

resultLab.grid(row=7, column = 0)
resultTXT.grid(row=8, column = 0)

root.mainloop()



