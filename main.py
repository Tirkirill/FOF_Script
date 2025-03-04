from CONSTS import WEAPONS, APP_NAME, NO_WEAPON, RANDOM_WEAPON
from generating_script import generate_script_file

from tkinter import *
from tkinter import ttk

def clicked():
    generate_script_file(
        weapon1_var.get(), 
        weapon2_var.get(),
        weapon3_var.get(),
        weapon4_var.get())
    
    window.quit()

choices:list[str] = [RANDOM_WEAPON, *list(WEAPONS.keys()), NO_WEAPON]

window = Tk()
window.title(APP_NAME)
window.geometry('420x170')

weapon1_var:StringVar = StringVar(value=choices[0])  
weapon2_var:StringVar = StringVar(value=choices[-1]) 
weapon3_var:StringVar = StringVar(value=choices[-1]) 
weapon4_var:StringVar = StringVar(value=choices[-1]) 

rows:int = 0

textbox:ttk.Label = ttk.Label(text="Стартовое оружие") 
textbox.grid(column=0, columnspan=2, row=rows, pady=3, padx=2) 
rows += 1

textbox:ttk.Label = ttk.Label(text="1 оружие") 
textbox.grid(column=0, row=rows, pady=3, padx=2) 
combobox:ttk.Combobox = ttk.Combobox(values=choices, textvariable=weapon1_var, state="readonly")
combobox.grid(column=1, row=rows, pady=3)
rows += 1

textbox:ttk.Label = ttk.Label(text="2 оружие") 
textbox.grid(column=0, row=rows, pady=3) 
combobox:ttk.Combobox = ttk.Combobox(values=choices, textvariable=weapon2_var, state="readonly")
combobox.grid(column=1, row=rows, pady=3)
rows += 1

textbox:ttk.Label = ttk.Label(text="3 оружие") 
textbox.grid(column=0, row=rows, pady=3) 
combobox:ttk.Combobox = ttk.Combobox(values=choices, textvariable=weapon3_var, state="readonly")
combobox.grid(column=1, row=rows, pady=3)
rows += 1

textbox:ttk.Label = ttk.Label(text="4 оружие") 
textbox.grid(column=0, row=rows, pady=3)
combobox:ttk.Combobox = ttk.Combobox(values=choices, textvariable=weapon4_var, state="readonly")
combobox.grid(column=1, row=rows, pady=3)
rows += 1

submit_button:Button = Button(window, text="Готово", command=clicked, justify="left") 
submit_button.grid(column=0, row=rows, pady=3, padx=5) 

window.mainloop()