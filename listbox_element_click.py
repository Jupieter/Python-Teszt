import tkinter as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("500x500")  # Size of the window 

def my_upd(my_widget):
    my_w = my_widget.widget
    index = int(my_w.curselection()[0])
    value = my_w.get(index)
    print ("You selected item ",index, value) 

def my_updel():
    l1.delete(ANCHOR)  # Delete selected element
    #l1.delete(2)  # Delete the 2nd position element     

my_font=('times', 8, 'italic')   
l1 = tk.Listbox(my_w, height=8, width=100, bg='yellow', bd=5, cursor='boat',
                font=my_font, fg='green',
                highlightcolor='blue', highlightthickness=15,
                selectbackground='orange', selectforeground='cyan',
                selectmode='multiple'
                #selectmode: It can be SINGLE, BROWSE, MULTIPLE, EXTENDED
                )
l1.pack(side=TOP, anchor=CENTER, ipady=0, ipadx=40) 
sb = Scrollbar(l1)
sb.pack(side=RIGHT, fill=Y)
l1.config(yscrollcommand=sb.set)
sb.config(command=l1.yview)
print(l1.pack_info () )

my_list=[('PHP',1),('Python',2),('MySQL',3),'JavaScript','JQuery','PHP','Python','MySQL']
for element in my_list:
    l1.insert(tk.END,element)
#l1.delete(0,END)     # Delete all elements 

#b1 = tk.Button(my_w, text="Delete", command=lambda l1=l1: l1.delete(ANCHOR))  #short method
b1 = tk.Button(my_w, text="Delete", command=lambda: my_updel())
b1.pack(side=TOP)

l1.bind('<<ListboxSelect>>', my_upd)
    
my_w.mainloop()  # Keep the window open
