import tkinter as tk
from PIL import ImageTk,Image
root=tk.Tk()

HEIGHT=500
WIDTH=600

def test_function(entry):
    print('This entry is',entry)

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image=tk.PhotoImage("images(1).png")
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)
background_label.pack()

frame=tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button=tk.Button(frame,text="Get Weather",font=40,command=lambda: test_function(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame=tk.Frame(root,bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lower_frame)
label.place(relwidth=1,relheight=1)

root.mainloop()
