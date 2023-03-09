from tkinter import *
from PIL import Image,ImageTk

from decorator import Decorator
from pizza_class import Pizza

from pizza_types.classic_pizza import ClassicPizza
from pizza_types.margherita_pizza import MargheritaPizza
from pizza_types.base_pizza import BasePizza
from pizza_types.turkish_pizza import TurkishPizza
from sauce_types.cheese import Cheese
from sauce_types.corn import Corn
from sauce_types.meat import Meat
from sauce_types.mushroom import Mushroom
from sauce_types.olive import Olive
from sauce_types.onion import Onion


def main():
    print('Menuyu yazdirir')

main()

form = Tk()
form.title('Pizza Dünyası')
form.geometry('750x750+450+50')
form.resizable(False,False)

menu_title=Label(form,text='Pizza Dünyasına Hoşgeldiniz',fg='darkred',font='Times 16 bold italic')
pizza_selection=Label(form,text='Lütfen Bir Pizza Tabanı Seçiniz',font='Times 12 italic')


menu_title.pack()
pizza_selection.pack()

classic_pizza=Image.open('images/classic_pizza.png')
pizza1_resize=classic_pizza.resize((110,110))
pizza1=ImageTk.PhotoImage(pizza1_resize)
label1=Label(form,image=pizza1).place(x=40,y=80)

classic=ClassicPizza()

pizza1_description=Label(form,text=classic.description,font='Times 12 italic',fg='black').place(x=160,y=125)
pizza1_price=Label(form,text=f'{classic.price} TL',font='Times 12 italic',fg='black').place(x=160,y=150)


int_vars = [IntVar() for i in range(10)]


button1=Checkbutton(form,variable=int_vars[0],onvalue=1,offvalue=0,command=lambda:select_pizza(classic)).place(x=220,y=150)


margherita_pizza=Image.open('images/margherita_pizza.png')
pizza2_resize=margherita_pizza.resize((110,110))
pizza2=ImageTk.PhotoImage(pizza2_resize)
label2=Label(form,image=pizza2).place(x=410,y=80)

margherita=MargheritaPizza()

pizza2_description=Label(form,text=margherita.description,font='Times 12 italic',fg='black').place(x=530,y=125)
pizza2_price=Label(form,text=f'{margherita.price} TL',font='Times 12 italic',fg='black').place(x=530,y=150)

button2=Checkbutton(form,variable=int_vars[1],onvalue=1,offvalue=0,command=lambda:select_pizza(margherita)).place(x=590,y=150)


base_pizza=Image.open('images/base_pizza.png')
pizza3_resize=base_pizza.resize((110,110))
pizza3=ImageTk.PhotoImage(pizza3_resize)
label3=Label(form,image=pizza3).place(x=40,y=220)

base=BasePizza()

pizza3_description=Label(form,text=base.description,font='Times 12 italic',fg='black').place(x=160,y=265)
pizza3_price=Label(form,text=f'{base.price} TL',font='Times 12 italic',fg='black').place(x=160,y=290)

button3=Checkbutton(form,variable=int_vars[2],onvalue=1,offvalue=0,command=lambda:select_pizza(base)).place(x=220,y=290)


turkish_pizza=Image.open('images/turkish_pizza.png')
pizza4_resize=turkish_pizza.resize((110,110))
pizza4=ImageTk.PhotoImage(pizza4_resize)
label4=Label(form,image=pizza4).place(x=410,y=220)

turkish=TurkishPizza()

pizza4_description=Label(form,text=turkish.description,font='Times 12 italic',fg='black').place(x=530,y=265)
pizza4_price=Label(form,text=f'{turkish.price} TL',font='Times 12 italic',fg='black').place(x=530,y=290)

button4=Checkbutton(form,variable=int_vars[3],onvalue=1,offvalue=0,command=lambda:select_pizza(turkish)).place(x=590,y=290)

selected_pizza=Pizza()


def select_pizza(selected_pizza):
    if int_vars[0].get()==1 or int_vars[1].get()==1 or int_vars[2].get()==1 or int_vars[3].get()==1:
        if selected_pizza==classic:
            print(str(selected_pizza.get_description()), int(selected_pizza.get_cost()))
        elif selected_pizza==margherita:
            print(str(selected_pizza.get_description()),int(selected_pizza.get_cost()))
        elif selected_pizza==base:
            print(str(selected_pizza.get_description()),int(selected_pizza.get_cost()))
        elif selected_pizza==turkish:
            print(str(selected_pizza.get_description()),int(selected_pizza.get_cost()))
        else:
            print('Lütfen bir seçim yapınız')

pizza_sauce_selection=Label(form,text='Lütfen Bir Pizza Sosu Seçiniz',font='Times 12 italic').place(x=270,y=350)

selected_sauce=Decorator(selected_pizza,selected_pizza.get_description(),selected_pizza.get_cost())

def add_sauce(selected_sauce):
   if selected_sauce==olive:
       print(selected_sauce.get_description(),selected_sauce.get_cost())
   elif selected_sauce==mushroom:
       print(selected_sauce.get_description(),selected_sauce.get_cost())
   elif selected_sauce==cheese:
       print(selected_sauce.get_description(),selected_sauce.get_cost())
   elif selected_sauce==meat:
       print(selected_sauce.get_description(),selected_sauce.get_cost())
   elif selected_sauce==onion:
       print(selected_sauce.get_description(),selected_sauce.get_cost())
   elif selected_sauce==corn:
       print(selected_sauce.get_description(),selected_sauce.get_cost())
   else:
       print('Lütfen bir seçim yapınız')

sauce_1=Image.open('images/olive.png')
sauce1_resize=sauce_1.resize((120,80))
olive_image=ImageTk.PhotoImage(sauce1_resize)
label5=Label(form,image=olive_image).place(x=50,y=400)

olive=Olive(selected_sauce)

olive_description=Label(form,text=olive.description,font='Times 12 italic',fg='black').place(x=175,y=420)
olive_price=Label(form,text=f'{olive.price} TL',font='Times 12 italic',fg='black').place(x=175,y=440)

button5=Checkbutton(form,variable=int_vars[4],onvalue=1,offvalue=0,
               command=lambda:add_sauce(olive)).place(x=225,y=440)

sauce_2=Image.open('images/mushroom.png')
sauce2_resize=sauce_2.resize((120,80))
mushroom_image=ImageTk.PhotoImage(sauce2_resize)
label6=Label(form,image=mushroom_image).place(x=275,y=400)


mushroom=Mushroom(selected_sauce)

mushroom_description=Label(form,text=mushroom.description,font='Times 12 italic',fg='black').place(x=400,y=420)
mushroom_price=Label(form,text=f'{mushroom.price} TL',font='Times 12 italic',fg='black').place(x=400,y=440)

button6=Checkbutton(form,variable=int_vars[5],onvalue=1,offvalue=0,command=lambda:add_sauce(mushroom)).place(x=450,y=440)


sauce_3=Image.open('images/cheese.png')
sauce3_resize=sauce_3.resize((120,80))
cheese_image=ImageTk.PhotoImage(sauce3_resize)
label7=Label(form,image=cheese_image).place(x=500,y=400)


cheese=Cheese(selected_sauce)

cheese_description=Label(form,text=cheese.description,font='Times 12 italic',fg='black').place(x=625,y=420)
cheese_price=Label(form,text=f'{cheese.price} TL',font='Times 12 italic',fg='black').place(x=625,y=440)

button7=Checkbutton(form,variable=int_vars[6],onvalue=1,offvalue=0,command=lambda:add_sauce(cheese)).place(x=675,y=440)


sauce_4=Image.open('images/meat.png')
sauce4_resize=sauce_4.resize((120,80))
meat_image=ImageTk.PhotoImage(sauce4_resize)
label8=Label(form,image=meat_image).place(x=50,y=550)

meat=Meat(selected_sauce)

meat_description=Label(form,text=meat.description,font='Times 12 italic',fg='black').place(x=175,y=570)
meat_price=Label(form,text=f'{meat.price} TL',font='Times 12 italic',fg='black').place(x=175,y=590)


button8=Checkbutton(form,variable=int_vars[7],onvalue=1,offvalue=0,command=lambda:add_sauce(meat)).place(x=225,y=590)

sauce_5=Image.open('images/onion.png')
sauce5_resize=sauce_5.resize((120,80))
onion_image=ImageTk.PhotoImage(sauce5_resize)
label9=Label(form,image=onion_image).place(x=275,y=550)

onion=Onion(selected_sauce)

onion_description=Label(form,text=onion.description,font='Times 12 italic',fg='black').place(x=400,y=570)
onion_price=Label(form,text=f'{onion.price} TL',font='Times 12 italic',fg='black').place(x=400,y=590)


button9=Checkbutton(form,variable=int_vars[8],onvalue=1,offvalue=0,command=lambda:add_sauce(onion)).place(x=450,y=590)

sauce_6=Image.open('images/corn.png')
sauce6_resize=sauce_6.resize((120,80))
corn_image=ImageTk.PhotoImage(sauce6_resize)
label10=Label(form,image=corn_image).place(x=500,y=550)

corn=Corn(selected_sauce)

corn_description=Label(form,text=corn.description,font='Times 12 italic',fg='black').place(x=625,y=570)
corn_price=Label(form,text=f'{corn.price} TL',font='Times 12 italic',fg='black').place(x=625,y=590)



button10=Checkbutton(form,variable=int_vars[9],onvalue=1,offvalue=0,command=lambda:add_sauce(corn)).place(x=675,y=590)



form.mainloop()

