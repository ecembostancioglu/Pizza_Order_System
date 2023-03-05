from tkinter import *
from PIL import Image,ImageTk

from klasik_pizza import KlasikPizza
from margarita_pizza import MargaritaPizza
from sade_pizza import SadePizza
from turk_pizza import TurkPizza


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

klasik=KlasikPizza(isim='Klasik Pizza',aciklama='Peynirli Pizza',fiyat='200 TL')

pizza1_isim=Label(form,text=klasik.isim,font='Times 14 bold italic',fg='darkred').place(x=160,y=100)
pizza1_aciklama=Label(form,text=klasik.aciklama,font='Times 12 italic',fg='black').place(x=160,y=125)
pizza1_fiyat=Label(form,text=klasik.fiyat,font='Times 12 italic',fg='black').place(x=160,y=150)




margarita_pizza=Image.open('images/margarita_pizza.png')
pizza2_resize=margarita_pizza.resize((100,100))
pizza2=ImageTk.PhotoImage(pizza2_resize)
label2=Label(form,image=pizza2).place(x=410,y=80)

margarita=MargaritaPizza(isim='Margarita Pizza',aciklama='Peynir ve Domatesli Pizza',fiyat='300 TL')

pizza2_isim=Label(form,text=margarita.isim,font='Times 14 bold italic',fg='darkred').place(x=530,y=100)
pizza2_aciklama=Label(form,text=margarita.aciklama,font='Times 12 italic',fg='black').place(x=530,y=125)
pizza2_fiyat=Label(form,text=margarita.fiyat,font='Times 12 italic',fg='black').place(x=530,y=150)




sade_pizza=Image.open('images/sade_pizza.png')
pizza3_resize=sade_pizza.resize((100,100))
pizza3=ImageTk.PhotoImage(pizza3_resize)
label3=Label(form,image=pizza3).place(x=40,y=220)

sade=SadePizza(isim='Sade Pizza',aciklama='Peynir ve Domates Soslu Pizza',fiyat='250 TL')

pizza3_isim=Label(form,text=sade.isim,font='Times 14 bold italic',fg='darkred').place(x=160,y=240)
pizza3_aciklama=Label(form,text=sade.aciklama,font='Times 12 italic',fg='black').place(x=160,y=265)
pizza3_fiyat=Label(form,text=sade.fiyat,font='Times 12 italic',fg='black').place(x=160,y=290)




turk_pizza=Image.open('images/turk_pizza.png')
pizza4_resize=turk_pizza.resize((100,100))
pizza4=ImageTk.PhotoImage(pizza4_resize)
label4=Label(form,image=pizza4).place(x=410,y=220)

turk=TurkPizza(isim='Türk Pizza',aciklama='Peynir ve Sucuklu Pizza',fiyat='400 TL')

pizza3_isim=Label(form,text=turk.isim,font='Times 14 bold italic',fg='darkred').place(x=530,y=240)
pizza4_aciklama=Label(form,text=turk.aciklama,font='Times 12 italic',fg='black').place(x=530,y=265)
pizza4_fiyat=Label(form,text=turk.fiyat,font='Times 12 italic',fg='black').place(x=530,y=290)





form.mainloop()

