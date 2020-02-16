from tkinter import *
from PIL import Image, ImageTk
from Fridge_Functions import *

app = Tk()
app.configure(bg = "#beebe9")
frame = Frame(app)
frame.grid()


def applyFunction():
    string_item = Item_Enter.get()
    int_quan = Quantity_Enter.get()
    pair_item_quan.append((str(string_item), int(int_quan)))
    print(type(Item_Enter))
    Item_Enter.delete(0, END)
    Quantity_Enter.delete(0, END)
    print(pair_item_quan)
    


app.geometry("1980x1080") 
#app_name = Label(app, text = "Cookle", fg = 'orange', font = ('Helvetica', 48))
g = Canvas(app, width = 1980, height = 50, bg = "#ffe3ed")
g.grid(row = 0, column = 0, columnspan = 1980)
r = Canvas(app, width = 300, height = 150, bg = "#fffdf9" )
#r1 = r.create_rectangle(100,100, 200,400, fill= "yellow")
r.place(x = 500, y = 300)
app_name = Label(app, text = "Cookle", fg = 'red', font = ('Helvetica', 48), bg = "#fffdf9")
app_name.place(x = 550, y = 350)
#r.grid(row = 100, column = 100)



unit_list = (
    'Single Item(s)',
    'Grams',
     'Kilograms',
     'Pounds',      
     'Liter',
     'Ounces',
     'Oz',
      )

Item = Label(app, text="Items", bg = "#ffe3ed").grid(row = 0, sticky = W)
Quantity = Label(app, text="Quantity", bg = "#ffe3ed").grid(row = 0, column = 2, sticky = W)
Unit = Label(app, text="Unit", bg = "#ffe3ed").grid(row = 0, column = 4)

pair_item_quan = []
Entry_Items  = StringVar()
Item_Enter = Entry(app, textvariable=Entry_Items)
Item_Enter.grid(row = 1, column = 1)



Entry_quantity = IntVar()
Quantity_Enter = Entry(app, textvariable=Entry_quantity)
Quantity_Enter.grid(row = 1, column = 3)


apply = Button(app, text="Apply", command=applyFunction).grid(row = 3)


Unit_choice = StringVar(app)
Unit_choice.set(unit_list[0])
Units = OptionMenu(app, Unit_choice, *unit_list).grid(row = 1, column = 4)


#path = "fridgeIMG.jpg"
#img = ImageTk.PhotoImage(Image.open(path))
#panel = Label(app, image = img).grid(row = 0) 



var = IntVar()

var1 = IntVar()

var2 = IntVar()

var3 = IntVar()

var4 = IntVar()

var5 = IntVar()

c = Checkbutton(app, text="Sad", variable = var, bg = "#ffe3ed")

c.grid(row = 0, column = 780)

c1 = Checkbutton(app, text="Happy", variable = var1, bg = "#ffe3ed")

c1.grid(row = 0, column = 790)

c2 = Checkbutton(app, text="Romance", variable = var2, bg = "#ffe3ed")

c2.grid(row = 0, column = 800)

c3 = Checkbutton(app, text="Hungry", variable = var3, bg = "#ffe3ed")

c3.grid(row = 0, column = 810)

c4 = Checkbutton(app, text="Angry", variable = var4, bg = "#ffe3ed")

c4.grid(row = 0, column = 820)

c5 = Checkbutton(app, text="Stressful", variable = var5, bg = "#ffe3ed")

c5.grid(row = 0, column = 830)
# command = onClick, Removed this from below
a=Button(app, text = "Apply")

a.grid(row = 1, column = 840)

app.mainloop()