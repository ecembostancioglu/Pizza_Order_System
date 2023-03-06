from tkinter import *
from PIL import Image,ImageTk

from pizza_types.klasik_pizza import KlasikPizza
from pizza_types.margarita_pizza import MargaritaPizza
from pizza_types.sade_pizza import SadePizza
from pizza_types.turk_pizza import TurkPizza
from sauce_types.cheese import Peynir
from sauce_types.mushroom import Mantar
from sauce_types.olive import Zeytin


def main():
    print('Menuyu yazdirir')

main()

form = Tk()
form.title('Pizza Dünyası')
form.geometry('750x750+450+50')
form.resizable(False,False)

menu_title=Label(form,text='Pizza Dünyasına Hoşgeldiniz',fg='darkred',font='Times 16 bold italic')
pizza_secimi=Label(form,text='Lütfen Bir Pizza Tabanı Seçiniz',font='Times 12 italic')




menu_title.pack()
pizza_secimi.pack()

klasik_pizza=Image.open('images/klasik_pizza.png')
pizza1_resize=klasik_pizza.resize((110,110))
pizza1=ImageTk.PhotoImage(pizza1_resize)
label1=Label(form,image=pizza1).place(x=40,y=80)

klasik=KlasikPizza(isim='Klasik Pizza',aciklama='Peynirli Pizza',fiyat='200 TL')

pizza1_isim=Label(form,text=klasik.isim,font='Times 14 bold italic',fg='darkred').place(x=160,y=100)
pizza1_aciklama=Label(form,text=klasik.aciklama,font='Times 12 italic',fg='black').place(x=160,y=125)
pizza1_fiyat=Label(form,text=klasik.fiyat,font='Times 12 italic',fg='black').place(x=160,y=150)




margarita_pizza=Image.open('images/margarita_pizza.png')
pizza2_resize=margarita_pizza.resize((110,110))
pizza2=ImageTk.PhotoImage(pizza2_resize)
label2=Label(form,image=pizza2).place(x=410,y=80)

margarita=MargaritaPizza(isim='Margarita Pizza',aciklama='Peynir ve Domatesli Pizza',fiyat='300 TL')

pizza2_isim=Label(form,text=margarita.isim,font='Times 14 bold italic',fg='darkred').place(x=530,y=100)
pizza2_aciklama=Label(form,text=margarita.aciklama,font='Times 12 italic',fg='black').place(x=530,y=125)
pizza2_fiyat=Label(form,text=margarita.fiyat,font='Times 12 italic',fg='black').place(x=530,y=150)




sade_pizza=Image.open('images/sade_pizza.png')
pizza3_resize=sade_pizza.resize((110,110))
pizza3=ImageTk.PhotoImage(pizza3_resize)
label3=Label(form,image=pizza3).place(x=40,y=220)

sade=SadePizza(isim='Sade Pizza',aciklama='Peynir ve Domates Soslu Pizza',fiyat='250 TL')

pizza3_isim=Label(form,text=sade.isim,font='Times 14 bold italic',fg='darkred').place(x=160,y=240)
pizza3_aciklama=Label(form,text=sade.aciklama,font='Times 12 italic',fg='black').place(x=160,y=265)
pizza3_fiyat=Label(form,text=sade.fiyat,font='Times 12 italic',fg='black').place(x=160,y=290)




turk_pizza=Image.open('images/turk_pizza.png')
pizza4_resize=turk_pizza.resize((110,110))
pizza4=ImageTk.PhotoImage(pizza4_resize)
label4=Label(form,image=pizza4).place(x=410,y=220)

turk=TurkPizza(isim='Türk Pizza',aciklama='Peynir ve Sucuklu Pizza',fiyat='400 TL')

pizza4_isim=Label(form,text=turk.isim,font='Times 14 bold italic',fg='darkred').place(x=530,y=240)
pizza4_aciklama=Label(form,text=turk.aciklama,font='Times 12 italic',fg='black').place(x=530,y=265)
pizza4_fiyat=Label(form,text=turk.fiyat,font='Times 12 italic',fg='black').place(x=530,y=290)


pizza_secimi=Label(form,text='Lütfen Bir Pizza Sosu Seçiniz',font='Times 12 italic').place(x=270,y=350)

sos_1=Image.open('images/zeytin.png')
sos1_resize=sos_1.resize((120,80))
zeytin_image=ImageTk.PhotoImage(sos1_resize)
label5=Label(form,image=zeytin_image).place(x=50,y=400)

zeytin=Zeytin(isim='Zeytin',fiyat='10 TL')
zeytin_isim=Label(form,text=zeytin.isim,font='Times 12 italic',fg='black').place(x=175,y=420)
zeytin_fiyat=Label(form,text=zeytin.fiyat,font='Times 12 italic',fg='black').place(x=175,y=440)



sos_2=Image.open('images/mantarlar.png')
sos2_resize=sos_2.resize((120,80))
mantar_image=ImageTk.PhotoImage(sos2_resize)
label6=Label(form,image=mantar_image).place(x=275,y=400)

mantar=Mantar(isim='Mantarlar',fiyat='40 TL')
mantar_isim=Label(form,text=mantar.isim,font='Times 12 italic',fg='black').place(x=400,y=420)
mantar_fiyat=Label(form,text=mantar.fiyat,font='Times 12 italic',fg='black').place(x=400,y=440)



sos_3=Image.open('images/peynir.png')
sos3_resize=sos_3.resize((120,80))
peynir_image=ImageTk.PhotoImage(sos3_resize)
label7=Label(form,image=peynir_image).place(x=500,y=400)

peynir=Peynir(isim='Keçi Peyniri',fiyat='50 TL')
peynir_isim=Label(form,text=peynir.isim,font='Times 12 italic',fg='black').place(x=625,y=420)
peynir_fiyat=Label(form,text=peynir.fiyat,font='Times 12 italic',fg='black').place(x=625,y=440)



sos_4=Image.open('images/et.png')
sos4_resize=sos_4.resize((120,80))
et_image=ImageTk.PhotoImage(sos4_resize)
label8=Label(form,image=et_image).place(x=100,y=550)


sos_5=Image.open('images/sogan.png')
sos5_resize=sos_5.resize((120,80))
sogan_image=ImageTk.PhotoImage(sos5_resize)
label9=Label(form,image=sogan_image).place(x=275,y=550)


sos_6=Image.open('images/misir.png')
sos6_resize=sos_6.resize((120,80))
misir_image=ImageTk.PhotoImage(sos6_resize)
label10=Label(form,image=misir_image).place(x=500,y=550)





form.mainloop()

