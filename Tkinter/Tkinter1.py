import tkinter

window=tkinter.Tk()
window.title("Tkinterinhooo")
window.configure(bg="purple")
window.configure(borderwidth=200)


def button_clicked():
    message=my_entry.get()
    print(message)


my_label=tkinter.Label(text="Joestar")
my_label.config(bg="purple",fg="White",font=("Arial",30,"italic"))
my_label.grid(row=1, column=1)
#my_label.pack()


my_button=tkinter.Button(text="Send",command=button_clicked)
my_button.grid(row=1, column=0)
#my_button.pack()


my_entry=tkinter.Entry(width=35)
my_entry.grid(row=1,column=2)
#my_entry.pack()








window.mainloop()