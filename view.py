import tkinter as tk

form = tk.Tk()
form.title('Pizza Dünyası')
form.geometry('500x500+500+100')
form.resizable(False,False)

menu_title=tk.Label(form,text='Pizza Dünyasına Hoşgeldiniz',fg='red',font='Times 18 bold italic')
menu_title.pack()




form.mainloop()

