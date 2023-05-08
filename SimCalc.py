# -*- coding: utf-8 -*-
"""
Simple Calculator
This is the first version.
Only include 4 main operators +, - ,* and /
does not include floating point as input
does not respond to keyboard
Created on Mon May  8 10:43:32 2023

@author: balali
"""


import customtkinter as ctk
import math

currentNumber = 0
lastNumber = 0
lastOperator = '+'

opr2List = ['+','-','*','/','^']
oprCalcList = ['=','C']
oprList = opr2List

def pressNumber(number):
    global currentNumber
    currentNumber = 10 * currentNumber + number
    updateScreen()


def opreator(opr):
    if opr == '+':
        return lambda x,y : x+y
    if opr == '-':
        return lambda x,y: x-y
    if opr == '*':
        return lambda x,y: x*y
    if opr == '/':
        return lambda x,y: x/y

    


def pressOpr(opr):
    global lastNumber
    global currentNumber
    global lastOperator
    if opr == '=':
        pressEqual()
        return 0
    if opr == 'C':
        pressC()
        return 1
    func = opreator(lastOperator)
    lastNumber = func(lastNumber,currentNumber)
    currentNumber = lastNumber
    updateScreen()
    currentNumber = 0
    lastOperator = opr
    return 2
    
def pressEqual():
    global lastNumber
    global currentNumber
    global lastOperator
    
    func = opreator(lastOperator)
    lastNumber = func(lastNumber,currentNumber)
    currentNumber = lastNumber
    updateScreen()
    currentNumber = 0
    lastOperator = '+'

def pressC():
    global lastNumber
    global currentNumber
    global lastOperator
    
    lastNumber = 0
    currentNumber = 0
    updateScreen()
    lastOperator = '+'

    
class calcNumButton(ctk.CTkButton):
    def __init__(self, parent, number, width = 10, height = 10):
        super().__init__(parent, text = str(number), width = width, height = height, command = lambda: pressNumber(number))
        


        
class calcOprButton(ctk.CTkButton):
    def __init__(self,parent,opr, width = 10, height = 10):
        super().__init__(parent,text = opr, width = width, height = height, command = lambda: pressOpr(opr))
        
        

def updateScreen():
    screen.delete(0,ctk.END)
    screen.insert(0,currentNumber)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

mainForm = ctk.CTk()
mainForm.title("Simple Calculator")
#mainForm.geometry("100*100")

#sizes 
sizeDict = {
    'button': (60,60),
    'screen': (320,60)
    }


screen = ctk.CTkEntry(mainForm, width=sizeDict['screen'][0],height=sizeDict['screen'][1], placeholder_text = "0")
screen.grid(row = 0,column =0, columnspan =2, padx =5, pady =5)


numButtonsFrame = ctk.CTkFrame(mainForm)
numButtonsFrame.grid(row = 1, column = 0, padx = 10,pady =10)

numButtons = []
numberPositions = []
for row in range(2,-1,-1):
    for col in range(3):
        numberPositions.append((row,col))
numberPositions.insert(0,(3,0))


for i in range(0,10):
    posx = numberPositions[i][0]
    posy = numberPositions[i][1]
    numButtons.append(calcNumButton(numButtonsFrame,i,width = sizeDict['button'][0],height = sizeDict['button'][1]))
    if (i==0):
        numButtons[-1].grid(row = posx, column = posy + 1, padx = 1,pady =1)
    else:
        numButtons[-1].grid(row = posx, column = posy, padx = 1,pady =1)



oprButtonsFrame = ctk.CTkFrame(mainForm)
oprButtonsFrame.grid(row = 1, column = 1, padx = 5, pady = 1)

oprPositions = [(3,0),(2,0),(1,0),(0,0)]
oprButtons = []
for i,pos in enumerate(oprPositions):
    posx = pos[0]
    posy = pos[1]
    oprButtons.append(calcOprButton(oprButtonsFrame,oprList[i],width=sizeDict['button'][0],height=sizeDict['button'][1]))
    oprButtons[-1].grid(row = posx, column = posy, padx = 1, pady =1)

equalButton = calcOprButton(oprButtonsFrame,'=',width=sizeDict['button'][0],height=sizeDict['button'][1])
equalButton.grid(row = 0, column = 1, padx = 1,pady =1)

CButton = calcOprButton(oprButtonsFrame,'C',width=sizeDict['button'][0],height=sizeDict['button'][1])
CButton.grid(row = 1, column = 1, padx = 1,pady =1)


reservedButton1 = ctk.CTkButton(numButtonsFrame,width = sizeDict['button'][0], height = sizeDict['button'][1],text = '')
reservedButton1.grid(row = 3 , column = 0, padx = 1, pady =1)

reservedButton2 = ctk.CTkButton(numButtonsFrame,width = sizeDict['button'][0], height = sizeDict['button'][1],text = '')
reservedButton2.grid(row = 3 , column = 2, padx = 1, pady =1)

reservedButton3 = ctk.CTkButton(oprButtonsFrame,width = sizeDict['button'][0], height = sizeDict['button'][1],text = '')
reservedButton3.grid(row = 2 , column = 1, padx = 1, pady =1)

reservedButton4 = ctk.CTkButton(oprButtonsFrame,width = sizeDict['button'][0], height = sizeDict['button'][1],text = '')
reservedButton4.grid(row = 3 , column = 1, padx = 1, pady =1)



mainForm.mainloop()
