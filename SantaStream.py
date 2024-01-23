# Kayla Mabalot
# 11 December 2023
# IS 340 Business Applications Programming
# Professor Phillips 

# SantaStream: Streaming Joy for the Holidays

#Set up basics: 

#Create main window
from tkinter import *
from datetime import datetime

mainWin = Tk()
mainWin.title('SantaStream')
mainWin.geometry("615x580") #window size

cc = IntVar()
fc = IntVar()
aa = IntVar()
rr = IntVar()
mm = IntVar()
ff = IntVar()
hh = IntVar()
rc = IntVar()
fg = IntVar()

moreClasses = StringVar()

# writeToFile()
def writeToFile():
    messagebox.showinfo(title=f"Processing...",message="Your order has been processed!")
    file = open('order.txt', 'a') # Append to file
    file.write('Customer Name: %s\n'         % name.get())
    file.write('Customer Email: %s\n'        % mail.get())
    file.write('Movie Types:\n'                          )
    if cc.get() == 1:
        file.write ('       Classic \n')
    if fc.get() == 1:
        file.write ('       Family Comedy \n')
    if aa.get() == 1:
        file.write ('       Animation \n')
    if rr.get() == 1:
        file.write ('       Romance \n')
    if mm.get() == 1:
        file.write ('       Musical \n')
    if ff.get() == 1:
        file.write ('       Fantasy \n')
    if hh.get() == 1:
        file.write ('       Horror \n')
    if rc.get() == 1:
        file.write ('       Romantic Comedy \n')
    if fg.get() == 1:
        file.write ('       Feel-Good \n')
    file.write('Card: %s\n'          % combo.get())
    now = datetime.now()
    file.write(f'Time: {now: %m/%d/%Y %I:%M %p} \n')
    file.write('=========================================\n')
    file.flush()
    file.close()
    resetFields()


# resetFields()  
#--------------------------------------------------------------
def resetFields():
    btnCC.deselect()
    btnFC.deselect()
    btnAA.deselect()
    btnRR.deselect()
    btnMM.deselect()
    btnFF.deselect()
    btnHH.deselect()
    btnRC.deselect()
    btnFG.deselect()
    #buttonA.deselect()
    buttonB.deselect()
    buttonC.deselect()
    buttonA.select()
    combo.set("")
    name.delete(0, END)
    mail.delete(0, END)
  
#ROW 0: Christmas Picture
img = PhotoImage (file='minion.png')
imgLbl = Label ( mainWin, image = img )
imgLbl.grid( row = 0, column =0, columnspan = 3 )

#ROW 1: Name Input
nameLabel = Label(mainWin, text="Name:",font=("Arial", 14, "bold"))
nameLabel.grid(row=1,column=0, sticky=E, pady=(20,20))
name = Entry(mainWin)
name.grid(row=1, column=1)

#ROW 2: Email Input
mailLabel = Label(mainWin, text="Email:",font=("Arial", 14, "bold"))
mailLabel.grid(row=2,column=0, sticky=E, pady=(20,20))
mail = Entry(mainWin)
mail.grid(row=2, column=1)

# ROW 4: Christmas Genres
# Movie Types: Classic, Family Comedy, Animation, Romance, Musical, Fantasy, Horror, Romantic Comedy, Feel-Good
 
movieLabel = Label(mainWin, text=" Christmas Genres: ", font=("Arial", 12, "bold"))
movieLabel.grid(row=4, column=0, sticky=W)

#ROW 5: Classic, Romance, Horror
btnCC = Checkbutton(mainWin, text='Classic', variable=cc, onvalue=1, offvalue=0, padx=10)
btnCC.grid(row=5, column=0, sticky=W)           #Classic

btnRR = Checkbutton(mainWin, text='Romance', variable=rr, onvalue=1, offvalue=0, padx=10)
btnRR.grid(row=5, column=1, sticky=W)           #Romance

btnHH = Checkbutton(mainWin, text='Horror', variable=hh, onvalue=1, offvalue=0, padx=10)
btnHH.grid(row=5, column=2, sticky=W)           #Horror

# ROW 6: Family Comedy, Musical, Romantic Comedy
btnFC = Checkbutton(mainWin, text='Family Comedy', variable=fc, onvalue=1, offvalue=0, padx=10)
btnFC.grid(row=6, column=0, sticky=W)           #Family Comedy

btnMM = Checkbutton(mainWin, text='Musical', variable=mm, onvalue=1, offvalue=0, padx=10)
btnMM.grid(row=6, column=1, sticky=W)           #Musical

btnRC = Checkbutton(mainWin, text='Romantic Comedy', variable=rc, onvalue=1, offvalue=0, padx=10)
btnRC.grid(row=6, column=2, sticky=W)           #Romantic Comedy

# ROW 7: Animation, Fantasy, Feel-Good
btnAA = Checkbutton(mainWin, text='Animation', variable=aa, onvalue=1, offvalue=0, padx=10)
btnAA.grid(row=7, column=0, sticky=W)

btnFF = Checkbutton(mainWin, text='Fantasy', variable=ff, onvalue=1, offvalue=0, padx=10)
btnFF.grid(row=7, column=1, sticky=W)           #Fantasy

btnFG = Checkbutton(mainWin, text='Feel-Good', variable=fg, onvalue=1, offvalue=0, padx=10)
btnFG.grid(row=7, column=2, sticky=W)           #Feel-Good

# ROW 8-11: Media Format
label2 = Label(mainWin, text="\n Media Format:",font=("Arial", 12, "bold"))
label3 = Label(mainWin, text="")

buttonstr = StringVar()

#Create 3 radiobuttons: Streaming, Blu-ray, DVD
buttonA = Radiobutton(mainWin, text = "Streaming", variable = buttonstr, value = "Streaming String")
buttonB = Radiobutton(mainWin, text = "Blue-ray", variable = buttonstr, value = "Blue-ray String")
buttonC = Radiobutton(mainWin, text = "DVD", variable = buttonstr, value = "DVD String")

#Function for Buttonstr Text
def showStr(event=None): 
  label3.config(text=buttonstr.get())
#Call the Function
buttonA.config(command=showStr)
buttonB.config(command=showStr)
buttonC.config(command=showStr)

buttonA.config(command=showStr)
buttonB.config(command=showStr)
buttonC.config(command=showStr)
 
# Position labels and buttons in the window
label2.grid (column=1, row=8)
buttonA.grid(column=0, row=9)
buttonB.grid(column=1, row=9)
buttonC.grid(column=2, row=9)
label3.grid (column=3, row=11)
buttonA.select() #Streaming selected by default

# ROW 11:Payment Method
# User Inputs and Preferences Pt.2
#Payment Method: Combobox
from tkinter import messagebox, ttk
import tkinter as tk
label4 = Label(mainWin, text=" \nPayment Method:",font=("Arial", 13, "bold"))
label4.grid (column=1, row=11)

def selection_changed(event):
    selection = combo.get()
combo = ttk.Combobox(values=["Visa","Credit or Debit Card","PayPal"])
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=190,y=525)

# ROW 12: Clear & Submit
clear = Button(mainWin, text='Clear',foreground="red", command=resetFields) # , command=resetFields 
clear.grid(row=11, column=2, sticky=E, pady=1)

submit = Button(mainWin, text='Submit',foreground="blue", command=writeToFile) # command=writeToFile 
submit.grid(row=12, column=2, sticky=E)


mainWin.mainloop()
