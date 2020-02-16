from tkinter import *
"""import PIL as pillow
from PIL import Image

im = Image.open("Computer.jpg")
"""
    
root = Tk()

def onClick():
    var = IntVar()
    
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    


    t = Checkbutton(root, text="Party", variable = var)
    t.grid(row = 100, column = 0)
    t1 = Checkbutton(root, text="Hungover", variable = var1)
    t1.grid(row = 100, column = 1)
    t2 = Checkbutton(root, text="Family", variable = var2)
    t2.grid(row = 100, column = 2)
    t3 = Checkbutton(root, text="Football", variable = var3)
    t3.grid(row = 100, column = 3)
    t4 = Checkbutton(root, text="Breakfast", variable = var4)
    t4.grid(row = 100, column = 4)
    t5 = Checkbutton(root, text="Date", variable = var5)
    t5.grid(row = 100, column = 5)
    t6 = Checkbutton(root, text="Binge", variable = var6)
    t6.grid(row = 100, column = 6)
    t7 = Checkbutton(root, text="Homealone", variable = var7)
    t7.grid(row = 100, column = 7)
    a1=Button(root, text = "Apply", command = onClick)
    a1.grid(row = 150, column = 10)

root.geometry("500x100")
topframe = Frame(root)
#topframe.pack(side = TOP)
scrollbar = Scrollbar()
"""entry = Entry(topframe)
entry.pack()"""

"""button = Button(topframe, text = "search")
button.pack(side = BOTTOM)"""

var = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()


c = Checkbutton(root, text="Sad", variable = var)
c.grid(row = 0, column = 0)
c1 = Checkbutton(root, text="Happy", variable = var1)
c1.grid(row = 0, column = 1)
c2 = Checkbutton(root, text="Romance", variable = var2)
c2.grid(row = 0, column = 2)
c3 = Checkbutton(root, text="Hungry", variable = var3)
c3.grid(row = 0, column = 3)
c4 = Checkbutton(root, text="Angry", variable = var4)
c4.grid(row = 0, column = 4)
c5 = Checkbutton(root, text="Stressful", variable = var5)
c5.grid(row = 0, column = 5)
a=Button(root, text = "Apply", command = onClick)
a.grid(row = 1, column = 6)


    
    
    
    
    

bottomframe = Frame(root)


scroll = Scrollbar(root)
#scroll.pack(side = RIGHT, fill = Y)
#text = Text(root)
#scroll.config(command = text.yview)
#text.pack()
#bottomframe.pack



root.mainloop()



