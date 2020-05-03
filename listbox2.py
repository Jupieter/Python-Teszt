import tkinter as tk
my_w = tk.Tk()
my_w.geometry("500x500")  # Size of the window 

def my_upd():
    print(l1.get(tk.ACTIVE))     # The selected element  
        
l1 = tk.Listbox(my_w,height=4)
l1.grid(row=1,column=1) 
my_list=['PHP','Python','MySQL']
for element in my_list:
    l1.insert(tk.END,element)

    
b1 = tk.Button(my_w, text='Show', width=10,bg='yellow',command=lambda: my_upd())
b1.grid(row=1,column=2) 

my_w.mainloop()  # Keep the window open
