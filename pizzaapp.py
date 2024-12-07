from tkinter import *
from tkinter.ttk import *

window=Tk()
window.minsize(700,500)
window.title('Table generator')

mainlabel = Label(window, text = 'Welcome to Pizza Picker! | Welcome! What would you like to order?')
mainlabel.grid(row = 1, column = 3)

pizzas = StringVar()

pizzadropdownbox = Combobox(window, textvariable = pizzas, width = 7)
pizzadropdownbox.grid(row = 3 , column = 2, padx = 15, pady = 15)

pizzadropdownbox['value'] = ['Margahrita', 'Peperoni', 'Sweetcorn']

pizzaamount = IntVar()

pizzaamountcombo = Combobox(window, textvariable = pizzaamount, width = 7)
pizzaamountcombo.grid(row = 2, column = 2)

pizzaamountcombo['values'] = tuple(range(11))

'''
rSM = Radiobutton(window, text = 'Small')
rME = Radiobutton(window, text = 'Medium')
rLA = Radiobutton(window, text = 'Large')
'''

#rSM.pack()
#rME.pack()
#rLA.pack()

orderbtn = Button(window, text = 'ORDER', command = None)



window.mainloop()
