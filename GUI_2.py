from tkinter import *   
from PIL import ImageTk,Image
gui=Tk() 
canvas=Canvas(gui,width=300,height=300)
canvas.pack()
img=ImageTk.PhotoImage(Image.open("escape.jpeg"))
canvas.create_image(30,20,anchor=NW,image=img)
gui.geometry("200x100")
def button_1():
    messagebox.showinfo("wrong")  
def button_2():
    messagebox.showinfo("elephant head")
def button_3():
    messagebox.showinfo("wrong")
def button_4():
    messagebox.showinfo("chair")
  
b1 = Button(gui,text = "bag",command = button_1,activeforeground = "red",activebackground = "pink",height=10,width=10)  
  
b2 = Button(gui, text = "elephant head",command=button_2,activeforeground = "blue",activebackground = "pink",height=10,width=10)  
  
b3 = Button(gui, text = "bed",command=button_3,activeforeground = "green",activebackground = "pink",height=10,width=10)  
  
b4 = Button(gui, text = "chair",command=button_4,activeforeground = "yellow",activebackground = "pink",height=10,width=10) 
b1.pack(side = LEFT)  
  
b2.pack(side = RIGHT)  
  
b3.pack(side = TOP)  
  
b4.pack(side = BOTTOM)

root.mainloop()
