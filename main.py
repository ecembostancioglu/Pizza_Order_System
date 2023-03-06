from tkinter import *
from PIL import Image,ImageTk

from decorator import Decorator

from pizza_types.classic_pizza import ClassicPizza
from pizza_types.margherita_pizza import MargheritaPizza
from pizza_types.sade_pizza import SadePizza
from pizza_types.turk_pizza import TurkPizza
from sauce_types.cheese import Cheese
from sauce_types.corn import Corn
from sauce_types.meat import Meat
from sauce_types.mushroom import Mushroom
from sauce_types.olive import Olive
from sauce_types.onion import Onion


def main():
    print('Menuyu yazdirir')

main()

def addToBasket():
    total=int(button1 + button2 + button3 + button4 + button5 + button6 + button7 + button8 + button9)
    print(total)  

form = Tk()
form.title('Pizza Dünyası')
form.geometry('750x750+450+50')
form.resizable(False,False)

menu_title=Label(form,text='Pizza Dünyasına Hoşgeldiniz',fg='darkred',font='Times 16 bold italic')
pizza_selection=Label(form,text='Lütfen Bir Pizza Tabanı Seçiniz',font='Times 12 italic')




menu_title.pack()
pizza_selection.pack()

klasik_pizza=Image.open('images/classic_pizza.png')
pizza1_resize=klasik_pizza.resize((110,110))
pizza1=ImageTk.PhotoImage(pizza1_resize)
label1=Label(form,image=pizza1).place(x=40,y=80)

classic=ClassicPizza(name='Klasik Pizza',description='Peynirli Pizza',price='200 TL')

pizza1_name=Label(form,text=classic.name,font='Times 14 bold italic',fg='darkred').place(x=160,y=100)
pizza1_description=Label(form,text=classic.description,font='Times 12 italic',fg='black').place(x=160,y=125)
pizza1_price=Label(form,text=classic.price,font='Times 12 italic',fg='black').place(x=160,y=150)

button1=Button(form,text='+',background='green',padx=10,command=classic.get_cost).place(x=220,y=150)



margherita_pizza=Image.open('images/margherita_pizza.png')
pizza2_resize=margherita_pizza.resize((110,110))
pizza2=ImageTk.PhotoImage(pizza2_resize)
label2=Label(form,image=pizza2).place(x=410,y=80)

margherita=MargheritaPizza(name='Margarita Pizza',description='Peynir ve Domatesli Pizza',price='300 TL')

pizza2_name=Label(form,text=margherita.name,font='Times 14 bold italic',fg='darkred').place(x=530,y=100)
pizza2_description=Label(form,text=margherita.description,font='Times 12 italic',fg='black').place(x=530,y=125)
pizza2_price=Label(form,text=margherita.price,font='Times 12 italic',fg='black').place(x=530,y=150)

button2=Button(form,text='+',background='green',padx=10,command=margherita.get_cost).place(x=590,y=150)


sade_pizza=Image.open('images/sade_pizza.png')
pizza3_resize=sade_pizza.resize((110,110))
pizza3=ImageTk.PhotoImage(pizza3_resize)
label3=Label(form,image=pizza3).place(x=40,y=220)

sade=SadePizza(name='Sade Pizza',description='Peynir ve Domates Soslu Pizza',price='250 TL')

pizza3_name=Label(form,text=sade.name,font='Times 14 bold italic',fg='darkred').place(x=160,y=240)
pizza3_description=Label(form,text=sade.description,font='Times 12 italic',fg='black').place(x=160,y=265)
pizza3_price=Label(form,text=sade.price,font='Times 12 italic',fg='black').place(x=160,y=290)

button3=Button(form,text='+',background='green',padx=10,command=sade.get_cost).place(x=220,y=290)


turk_pizza=Image.open('images/turk_pizza.png')
pizza4_resize=turk_pizza.resize((110,110))
pizza4=ImageTk.PhotoImage(pizza4_resize)
label4=Label(form,image=pizza4).place(x=410,y=220)

turk=TurkPizza(name='Türk Pizza',description='Peynir ve Sucuklu Pizza',price='400 TL')

pizza4_name=Label(form,text=turk.name,font='Times 14 bold italic',fg='darkred').place(x=530,y=240)
pizza4_description=Label(form,text=turk.description,font='Times 12 italic',fg='black').place(x=530,y=265)
pizza4_price=Label(form,text=turk.price,font='Times 12 italic',fg='black').place(x=530,y=290)

button4=Button(form,text='+',background='green',padx=10,command=turk.get_cost).place(x=590,y=290)


pizza_sauce_secimi=Label(form,text='Lütfen Bir Pizza Sosu Seçiniz',font='Times 12 italic').place(x=270,y=350)

sauce_1=Image.open('images/olive.png')
sauce1_resize=sauce_1.resize((120,80))
olive_image=ImageTk.PhotoImage(sauce1_resize)
label5=Label(form,image=olive_image).place(x=50,y=400)

olive=Olive(name='Zeytin',price='10 TL')
olive_name=Label(form,text=olive.name,font='Times 12 italic',fg='black').place(x=175,y=420)
olive_price=Label(form,text=olive.price,font='Times 12 italic',fg='black').place(x=175,y=440)

button5=Button(form,text='+',background='green',padx=10,command=olive.get_cost).place(x=180,y=465)

sauce_2=Image.open('images/mushroom.png')
sauce2_resize=sauce_2.resize((120,80))
mushroom_image=ImageTk.PhotoImage(sauce2_resize)
label6=Label(form,image=mushroom_image).place(x=275,y=400)

mushroom=Mushroom(name='Mantarlar',price='40 TL')
mushroom_name=Label(form,text=mushroom.name,font='Times 12 italic',fg='black').place(x=400,y=420)
mushroom_price=Label(form,text=mushroom.price,font='Times 12 italic',fg='black').place(x=400,y=440)

button6=Button(form,text='+',background='green',padx=10,command=mushroom.get_cost).place(x=405,y=465)


sauce_3=Image.open('images/cheese.png')
sauce3_resize=sauce_3.resize((120,80))
cheese_image=ImageTk.PhotoImage(sauce3_resize)
label7=Label(form,image=cheese_image).place(x=500,y=400)

cheese=Cheese(name='Keçi Peyniri',price='50 TL')
cheese_name=Label(form,text=cheese.name,font='Times 12 italic',fg='black').place(x=625,y=420)
cheese_price=Label(form,text=cheese.price,font='Times 12 italic',fg='black').place(x=625,y=440)

button6=Button(form,text='+',background='green',padx=10,command=cheese.get_cost).place(x=630,y=465)



sauce_4=Image.open('images/meat.png')
sauce4_resize=sauce_4.resize((120,80))
meat_image=ImageTk.PhotoImage(sauce4_resize)
label8=Label(form,image=meat_image).place(x=50,y=550)

meat=Meat(name='Et',price='100 TL')

meat_name=Label(form,text=meat.name,font='Times 12 italic',fg='black').place(x=175,y=570)
meat_price=Label(form,text=meat.price,font='Times 12 italic',fg='black').place(x=175,y=590)


button7=Button(form,text='+',background='green',padx=10,command=meat.get_cost).place(x=180,y=615)



sauce_5=Image.open('images/onion.png')
sauce5_resize=sauce_5.resize((120,80))
onion_image=ImageTk.PhotoImage(sauce5_resize)
label9=Label(form,image=onion_image).place(x=275,y=550)

onion=Onion(name='Soğan',price='25 TL')
onion_name=Label(form,text=onion.name,font='Times 12 italic',fg='black').place(x=400,y=570)
onion_price=Label(form,text=onion.price,font='Times 12 italic',fg='black').place(x=400,y=590)


button8=Button(form,text='+',background='green',padx=10,command=onion.get_cost).place(x=405,y=615)



sauce_6=Image.open('images/corn.png')
sauce6_resize=sauce_6.resize((120,80))
corn_image=ImageTk.PhotoImage(sauce6_resize)
label10=Label(form,image=corn_image).place(x=500,y=550)

corn=Corn(name='Mısır',price='30 TL')
corn_name=Label(form,text=corn.name,font='Times 12 italic',fg='black').place(x=625,y=570)
corn_price=Label(form,text=corn.price,font='Times 12 italic',fg='black').place(x=625,y=590)


button9=Button(form,text='+',background='green',padx=10,command=corn.get_cost).place(x=630,y=615)



form.mainloop()

