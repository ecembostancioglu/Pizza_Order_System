from tkinter import *
from PIL import Image,ImageTk


form = Tk()
form.title('Pizza Dünyası')
form.geometry('720x700+450+50')
form.resizable(False,False)

menu_title=Label(form,text='Pizza Dünyasına Hoşgeldiniz',fg='darkred',font='Times 18 bold italic')
pizza_secimi=Label(form,text='Lütfen Bir Pizza Tabanı Seçiniz',font='Times 14 italic')



menu_title.pack()
pizza_secimi.pack()

klasik_pizza=Image.open('images/klasik_pizza.png')
pizza1_resize=klasik_pizza.resize((100,100))
pizza1=ImageTk.PhotoImage(pizza1_resize)
label1=Label(form,image=pizza1).place(x=40,y=80)
pizza1_isim=Label(form,text='Klasik Pizza',font='Times 14 bold italic',fg='darkred').place(x=160,y=100)
pizza1_aciklama=Label(form,text='Peynirli Pizza',font='Times 12 italic',fg='black').place(x=160,y=125)




margarita_pizza=Image.open('images/margarita_pizza.png')
pizza2_resize=margarita_pizza.resize((100,100))
pizza2=ImageTk.PhotoImage(pizza2_resize)
label2=Label(form,image=pizza2).place(x=410,y=80)
pizza2_isim=Label(form,text='Margarita Pizza',font='Times 14 bold italic',fg='darkred').place(x=530,y=100)
pizza2_aciklama=Label(form,text='Peynir ve Domatesli Pizza',font='Times 12 italic',fg='black').place(x=530,y=125)



sade_pizza=Image.open('images/sade_pizza.png')
pizza3_resize=sade_pizza.resize((100,100))
pizza3=ImageTk.PhotoImage(pizza3_resize)
label3=Label(form,image=pizza3).place(x=40,y=220)
pizza3_isim=Label(form,text='Sade Pizza',font='Times 14 bold italic',fg='darkred').place(x=160,y=240)
pizza3_aciklama=Label(form,text='Peynir ve Domates Soslu Pizza',font='Times 12 italic',fg='black').place(x=160,y=265)



turk_pizza=Image.open('images/turk_pizza.png')
pizza4_resize=turk_pizza.resize((100,100))
pizza4=ImageTk.PhotoImage(pizza4_resize)
label4=Label(form,image=pizza4).place(x=410,y=220)
pizza3_isim=Label(form,text='Turk Pizza',font='Times 14 bold italic',fg='darkred').place(x=530,y=240)
pizza4_aciklama=Label(form,text='Peynir ve Sucuklu Pizza',font='Times 12 italic',fg='black').place(x=530,y=265)




form.mainloop()

