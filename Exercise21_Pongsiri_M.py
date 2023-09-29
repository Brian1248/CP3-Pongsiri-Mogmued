from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    labelResultBMI.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if result >= 30:
        labelResult.configure(text="อ้วนมาก!")
    elif result > 25:
        labelResult.configure(text="อ้วน")
    elif result > 23:
        labelResult.configure(text="น้ำหนักเกิน")
    elif result > 18.5:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif result <= 18.5:
        labelResult.configure(text="ผอมเกินไป!!")



MainWindow = Tk()
labelHeight = Label(MainWindow, text = "Height (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=2)
labelWeight = Label(MainWindow, text = "Weight (kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=2)
calculateButton = Button(MainWindow, text = "Calculation")
calculateButton.bind("<Button-1>",leftClickButton)
calculateButton.grid(row=2,column=0)
labelResultBMI = Label(MainWindow, text="ค่าดัชนีมวลกาย")
labelResultBMI.grid(row=2,column=2)
labelResult = Label(MainWindow)
labelResult.grid(row=3,column=2)


MainWindow.mainloop()
