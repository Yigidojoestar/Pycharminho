import tkinter

window = tkinter.Tk()
window.title("Tkintera")
window.configure(bg="White",borderwidth=200)
window.config(padx=20,pady=20)

label = tkinter.Label(text="Lvbel C5")
label.config(fg="Black")
label.config(bg="White")
label.config(padx=20,pady=20)
label.pack()


def buttonclicked():
    print(f"Title:{entry.get()}")
    print(text.get("1.0",tkinter.END))


button=tkinter.Button(text="Button",command=buttonclicked)
button.config(pady=20,padx=20)
button.config(fg="White",bg="Black")
button.pack()

entry=tkinter.Entry(width=20)
entry.config(fg="White",bg="Black")
entry.focus()
entry.pack()

text=tkinter.Text(width=30,height=10)
text.config(fg="White",bg="Black")
text.pack()

scale=tkinter.Scale(from_=0, to=50)
scale.pack()


spinbox=tkinter.Spinbox(from_=0,to=50)
spinbox.pack()

def checkbuttoninho():
    print(check_state.get())

check_state=tkinter.IntVar()
checkbutton=tkinter.Checkbutton(text="Kabul Ediyorum",variable=check_state,command=checkbuttoninho)
checkbutton.pack()


def raidoşeysi():
    print(radio_state.get())

radio_state=tkinter.IntVar()
radio_button=tkinter.Radiobutton(text="Oha",value=10,variable=radio_state,command=raidoşeysi)
radio_button2=tkinter.Radiobutton(text="Oba",value=20,variable=radio_state,command=raidoşeysi)
radio_button.pack()
radio_button2.pack()

def listbox_selected(event):
    print(listbox.get(listbox.curselection()))

listbox=tkinter.Listbox()
selam_list=["Merhaba","Hi","Salam"]
for i in range(len(selam_list)):
    listbox.insert(i,selam_list[i])
listbox.bind("<<ListboxSelect>>",listbox_selected)
listbox.pack()

tkinter.mainloop()
