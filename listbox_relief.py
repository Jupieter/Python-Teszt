#relief  
import tkinter as tk
my_w = tk.Tk()
my_w.geometry("200x400") 

l1 = tk.Label(my_w,  text='relief' ) 
l1.grid(row=1,column=1) 

l1 = tk.Label(my_w,  text='raised' ) 
l1.grid(row=2,column=1)
l1 = tk.Listbox(my_w,height=3,relief='raised')
l1.grid(row=2,column=2) 

l1.insert(1,'PHP')  
l1.insert(2,'Python')
l1.insert(3,'MySQL')

l1 = tk.Label(my_w,  text='sunken' ) 
l1.grid(row=3,column=1)
l2 = tk.Listbox(my_w,height=3,relief='sunken')
l2.grid(row=3,column=2) 

l2.insert(1,'PHP')  
l2.insert(2,'Python')
l2.insert(3,'MySQL')

l1 = tk.Label(my_w,  text='flat' ) 
l1.grid(row=4,column=1)
l3 = tk.Listbox(my_w,height=3,relief='flat')
l3.grid(row=4,column=2) 


l3.insert(1,'PHP')  
l3.insert(2,'Python')
l3.insert(3,'MySQL')

l1 = tk.Label(my_w,  text='ridge' ) 
l1.grid(row=5,column=1)
l4 = tk.Listbox(my_w,height=3,relief='ridge')
l4.grid(row=5,column=2) 

l4.insert(1,'PHP')  
l4.insert(2,'Python')
l4.insert(3,'MySQL')

l1 = tk.Label(my_w,  text='solid' ) 
l1.grid(row=6,column=1)
l5 = tk.Listbox(my_w,height=3,relief='solid')
l5.grid(row=6,column=2) 

l5.insert(1,'PHP')  
l5.insert(2,'Python')
l5.insert(3,'MySQL')

l1 = tk.Label(my_w,  text='groove' ) 
l1.grid(row=7,column=1)
l6 = tk.Listbox(my_w,height=3,relief='groove')
l6.grid(row=7,column=2) 

l6.insert(1,'PHP')  
l6.insert(2,'Python')
l6.insert(3,'MySQL')

my_w.mainloop() 
