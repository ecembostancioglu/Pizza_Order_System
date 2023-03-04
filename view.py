from tkinter import *
from PIL import Image,ImageTk


form = Tk()
form.title('Pizza Dünyası')
form.geometry('700x700+450+50')
form.resizable(False,False)

menu_title=Label(form,text='Pizza Dünyasına Hoşgeldiniz',fg='red',font='Times 18 bold italic')
pizza_secimi=Label(form,text='Lütfen Bir Pizza Tabanı Seçiniz',font='Times 14 italic')



menu_title.pack()
pizza_secimi.pack()

klasik_pizza=Image.open('images/klasik_pizza.png')
pizza1_resize=klasik_pizza.resize((100,100))
pizza1=ImageTk.PhotoImage(pizza1_resize)
label1=Label(form,image=pizza1).place(x=100,y=80)
pizza1_isim=Label(form,text='Klasik Pizza').place(x=115,y=180)




margarita_pizza=Image.open('images/margarita_pizza.png')
pizza2_resize=margarita_pizza.resize((100,100))
pizza2=ImageTk.PhotoImage(pizza2_resize)
label2=Label(form,image=pizza2).place(x=300,y=80)
pizza2_isim=Label(form,text='Margarita Pizza').place(x=310,y=180)



sade_pizza=Image.open('images/sade_pizza.png')
pizza3_resize=sade_pizza.resize((100,100))
pizza3=ImageTk.PhotoImage(pizza3_resize)
label3=Label(form,image=pizza3).place(x=100,y=230)
pizza3_isim=Label(form,text='Sade Pizza').place(x=120,y=330)



turk_pizza=Image.open('images/turk_pizza.png')
pizza4_resize=turk_pizza.resize((100,100))
pizza4=ImageTk.PhotoImage(pizza4_resize)
label4=Label(form,image=pizza4).place(x=300,y=230)
pizza3_isim=Label(form,text='Turk Pizza').place(x=322,y=330)




form.mainloop()

