from tkinter import *
from PIL import Image,ImageTk
import csv
from datetime import datetime


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


def main(): # Main function
    print('Menu')

main()

form = Tk() 
form.title('Pizza World') # Form title
form.configure(background='#F8F4EA') # Form background color
form.geometry('750x750+450+50') # Form size 
form.resizable(False,False)

menu_title=Label(form,text='Welcome to Pizza World',fg='darkred',font='Times 16 bold italic',bg='#F8F4EA')
pizza_selection=Label(form,text='Please Choose a Pizza Base',font='Times 12 italic',bg='#F8F4EA')


menu_title.pack()
pizza_selection.pack()

classic_pizza=Image.open('images/classic_pizza.png') # Classic Pizza image
pizza1_resize=classic_pizza.resize((110,110)) # Classic Pizza image size
pizza1=ImageTk.PhotoImage(pizza1_resize)
label1=Label(form,image=pizza1,bg='#F8F4EA').place(x=40,y=80)

classic=ClassicPizza() # An object from the Classic Pizza class

pizza1_description=Label(form,text=classic.description,font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=160,y=125) 
pizza1_price=Label(form,text=f'{classic.price} TL',font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=160,y=150)


int_vars = [IntVar() for i in range(10)] # List of numbers from 1 to 10 from the Intvar class


button1=Checkbutton(form,variable=int_vars[0],onvalue=1,offvalue=0,command=lambda:select_pizza(classic),bg='#F8F4EA').place(x=220,y=150)


margherita_pizza=Image.open('images/margherita_pizza.png')
pizza2_resize=margherita_pizza.resize((110,110))
pizza2=ImageTk.PhotoImage(pizza2_resize)
label2=Label(form,image=pizza2,bg='#F8F4EA').place(x=410,y=80)

margherita=MargheritaPizza()

pizza2_description=Label(form,text=margherita.description,font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=530,y=125)
pizza2_price=Label(form,text=f'{margherita.price} TL',font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=530,y=150)

button2=Checkbutton(form,variable=int_vars[1],onvalue=1,offvalue=0,command=lambda:select_pizza(margherita),bg='#F8F4EA').place(x=590,y=150)


base_pizza=Image.open('images/base_pizza.png')
pizza3_resize=base_pizza.resize((110,110))
pizza3=ImageTk.PhotoImage(pizza3_resize)
label3=Label(form,image=pizza3,bg='#F8F4EA').place(x=40,y=220)

base=BasePizza()

pizza3_description=Label(form,text=base.description,font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=160,y=265)
pizza3_price=Label(form,text=f'{base.price} TL',font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=160,y=290)

button3=Checkbutton(form,variable=int_vars[2],onvalue=1,offvalue=0,command=lambda:select_pizza(base),bg='#F8F4EA').place(x=220,y=290)


turkish_pizza=Image.open('images/turkish_pizza.png')
pizza4_resize=turkish_pizza.resize((110,110))
pizza4=ImageTk.PhotoImage(pizza4_resize)
label4=Label(form,image=pizza4,bg='#F8F4EA').place(x=410,y=220)

turkish=TurkishPizza()

pizza4_description=Label(form,text=turkish.description,font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=530,y=265)
pizza4_price=Label(form,text=f'{turkish.price} TL',font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=530,y=290)

button4=Checkbutton(form,variable=int_vars[3],onvalue=1,offvalue=0,command=lambda:select_pizza(turkish),bg='#F8F4EA').place(x=590,y=290)

selected_pizza=Pizza()

global pizza_price #a variable passed to another page
pizza_price=0
global pizza_desc #a variable passed to another page
pizza_desc=''

#Choose pizza base
def select_pizza(selected_pizza): 

    global pizza_price
    global pizza_desc

    if int_vars[0].get()==1 or int_vars[1].get()==1 or int_vars[2].get()==1 or int_vars[3].get()==1:
        pizza_price = int(selected_pizza.get_cost())
        pizza_desc=str(selected_pizza.get_description())
        amount_text.config(text=f'Total: {pizza_price} TL')
        summary_text.config(text=f'Ingredients: {pizza_desc}, ')

        pizza_price=int(selected_pizza.get_cost())
        pizza_desc=str(selected_pizza.get_description())
        
        if selected_pizza==classic:
            print(str(selected_pizza.get_description()), int(selected_pizza.get_cost()))
        elif selected_pizza==margherita:
            print(str(selected_pizza.get_description()),int(selected_pizza.get_cost()))
        elif selected_pizza==base:
            print(str(selected_pizza.get_description()),int(selected_pizza.get_cost()))
        elif selected_pizza==turkish:
            print(str(selected_pizza.get_description()),int(selected_pizza.get_cost()))
        else:
            print('Please choose a pizza base')

pizza_sauce_selection=Label(form,text='Please Choose a Pizza Sauce',font='Times 12 italic',bg='#F8F4EA').place(x=270,y=350)

selected_sauce=Decorator()

# Choose sauce
def add_sauce(selected_sauce):

    global pizza_price
    global pizza_desc

    sauce_price = int(selected_sauce.price)
    total_price=pizza_price + sauce_price
    pizza_price = total_price

    sauce_desc=str(selected_sauce.description)
    total_desc=pizza_desc + ',' + ' ' + sauce_desc
    pizza_desc=total_desc

    print(f'Pizza price:{pizza_price}')
    amount_text.config(text=f'Sepet Tutarı: {total_price} TL')
    summary_text.config(text=f'Sepet: {pizza_desc}')
    if selected_sauce==olive:
       print(selected_sauce.description,selected_sauce.price)
    elif selected_sauce==mushroom:
       print(selected_sauce.description,selected_sauce.price)
    elif selected_sauce==cheese:
       print(selected_sauce.description,selected_sauce.price)
    elif selected_sauce==meat:
       print(selected_sauce.description,selected_sauce.price)
    elif selected_sauce==onion:
       print(selected_sauce.description,selected_sauce.price)
    elif selected_sauce==corn:
       print(selected_sauce.description,selected_sauce.price)
    else:
       print('Please choose a sauce')

sauce_1=Image.open('images/olive.png')
sauce1_resize=sauce_1.resize((120,80))
olive_image=ImageTk.PhotoImage(sauce1_resize)
label5=Label(form,image=olive_image,bg='#F8F4EA').place(x=50,y=400)

olive=Olive()

olive_description=Label(form,text=olive.description,font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=175,y=420)
olive_price=Label(form,text=f'{olive.price} TL',font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=175,y=440)

button5=Checkbutton(form,variable=int_vars[4],onvalue=1,offvalue=0,
               command=lambda:add_sauce(olive),bg='#F8F4EA').place(x=225,y=440)

sauce_2=Image.open('images/mushroom.png')
sauce2_resize=sauce_2.resize((120,80))
mushroom_image=ImageTk.PhotoImage(sauce2_resize)
label6=Label(form,image=mushroom_image,bg='#F8F4EA').place(x=275,y=400)


mushroom=Mushroom()

mushroom_description=Label(form,text=mushroom.description,font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=400,y=420)
mushroom_price=Label(form,text=f'{mushroom.price} TL',font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=400,y=440)

button6=Checkbutton(form,variable=int_vars[5],onvalue=1,offvalue=0,command=lambda:add_sauce(mushroom),bg='#F8F4EA').place(x=450,y=440)


sauce_3=Image.open('images/cheese.png')
sauce3_resize=sauce_3.resize((120,80))
cheese_image=ImageTk.PhotoImage(sauce3_resize)
label7=Label(form,image=cheese_image,bg='#F8F4EA').place(x=500,y=400)


cheese=Cheese()

cheese_description=Label(form,text=cheese.description,font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=625,y=420)
cheese_price=Label(form,text=f'{cheese.price} TL',font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=625,y=440)

button7=Checkbutton(form,variable=int_vars[6],onvalue=1,offvalue=0,command=lambda:add_sauce(cheese),bg='#F8F4EA').place(x=675,y=440)


sauce_4=Image.open('images/meat.png')
sauce4_resize=sauce_4.resize((120,80))
meat_image=ImageTk.PhotoImage(sauce4_resize)
label8=Label(form,image=meat_image,bg='#F8F4EA').place(x=50,y=550)

meat=Meat()

meat_description=Label(form,text=meat.description,font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=175,y=570)
meat_price=Label(form,text=f'{meat.price} TL',font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=175,y=590)


button8=Checkbutton(form,variable=int_vars[7],onvalue=1,offvalue=0,command=lambda:add_sauce(meat),bg='#F8F4EA').place(x=225,y=590)
sauce_5=Image.open('images/onion.png')
sauce5_resize=sauce_5.resize((120,80))
onion_image=ImageTk.PhotoImage(sauce5_resize)
label9=Label(form,image=onion_image,bg='#F8F4EA').place(x=275,y=550)

onion=Onion()

onion_description=Label(form,text=onion.description,font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=400,y=570)
onion_price=Label(form,text=f'{onion.price} TL',font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=400,y=590)


button9=Checkbutton(form,variable=int_vars[8],onvalue=1,offvalue=0,command=lambda:add_sauce(onion),bg='#F8F4EA').place(x=450,y=590)

sauce_6=Image.open('images/corn.png')
sauce6_resize=sauce_6.resize((120,80))
corn_image=ImageTk.PhotoImage(sauce6_resize)
label10=Label(form,image=corn_image,bg='#F8F4EA').place(x=500,y=550)

corn=Corn()

corn_description=Label(form,text=corn.description,font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=625,y=570)
corn_price=Label(form,text=f'{corn.price} TL',font='Times 12 italic',fg='black',bg='#F8F4EA').place(x=625,y=590)


button10=Checkbutton(form,variable=int_vars[9],onvalue=1,offvalue=0,command=lambda:add_sauce(corn),bg='#F8F4EA').place(x=675,y=590)


amount_text=Label(form,text=f'Basket Amount:',font='Times 12 italic',fg='black',bg='#F8F4EA')
amount_text.place(x=300,y=680)

summary_text=Label(form,text=f'Amount:',font='Times 12 italic',fg='black',bg='#F8F4EA')
summary_text.place(x=300,y=650)

# Payment Button function 
def to_second_page(value,desc):
    global total_var
    global basket_price
    form.withdraw()
    second_page.deiconify()
    total_var=desc
    basket_price=value
    Label(second_page, text=f"{desc}",bg='#F8F4EA').place(x=400,y=240)
    Label(second_page, text=f"{value} TL",bg='#F8F4EA').place(x=400,y=280)


    second_page.mainloop() #Second Page was created

button11=Button(form,text='Payment',command=lambda:to_second_page(pizza_price,pizza_desc),bg='#F8F4EA').place(x=650,y=680)


second_page=Toplevel(form)
second_page.withdraw()


second_page.title('Payment Page')
second_page.geometry('750x750+450+50')
second_page.configure(background='#F8F4EA')
second_page.resizable(False,False)

payment=Label(second_page,text='Make the Payment',fg='darkred',font='Times 16 bold italic',bg='#F8F4EA').pack()


name_var=StringVar()
id_var=StringVar()
credit_var=StringVar()
password_var=StringVar()
total_var=StringVar()
basket_price=StringVar()

#Get User's Information
name_label=Label(second_page,text=f'Name:',bg='#F8F4EA')
name_label.place(x=200,y=80)
name_label.config(text=f'Name:')
name_entry=Entry(second_page,bg='#F8F4EA',textvariable=name_var).place(x=400,y=80)

id_label=Label(second_page,text=f'ID Number:',bg='#F8F4EA')
id_label.place(x=200,y=120)
id_label.config(text=f'ID Number:')
id_entry=Entry(second_page,bg='#F8F4EA',textvariable=id_var).place(x=400,y=120)

credit_label=Label(second_page,text=f'Credit Card Number:',bg='#F8F4EA')
credit_label.place(x=200,y=160)
credit_label.config(text=f'Credit Card Number:')
credit_entry=Entry(second_page,bg='#F8F4EA',textvariable=credit_var).place(x=400,y=160)

password_label=Label(second_page,text=f'Credit Card Password:',bg='#F8F4EA')
password_label.place(x=200,y=200)
password_label.config(text=f'Credit Card Password:')
password_entry=Entry(second_page,bg='#F8F4EA',textvariable=password_var,show = '*').place(x=400,y=200)

Label(second_page, text='Pizza and Ingredients:',bg='#F8F4EA').place(x=200,y=240)
Label(second_page, text='Total:',bg='#F8F4EA').place(x=200,y=280)


payment_button=Button(second_page,text='Payment',bg='#F8F4EA',height=1,width=10,
                      command=lambda:write_csv(total_var,basket_price)).place(x=350,y=360)


order1=Image.open('images/pizza.png')
order1_resize=order1.resize((120,120))
order1_image=ImageTk.PhotoImage(order1_resize)

order2=Image.open('images/cook.png')
order2_resize=order2.resize((120,120))
order2_image=ImageTk.PhotoImage(order2_resize)

order_label=Label(second_page,text='',font='Times 12 italic',bg='#F8F4EA')
order_label.place(x=300,y=400)


date=datetime.now() 
now_date=date.strftime('%Y-%m-%d %H:%M')


def write_csv(total,price):
   name=name_var.get()
   id=id_var.get()
   credit=credit_var.get()
   password=password_var.get()

   with open('Order_Database.csv','w') as my_file:  # Open .csv file
      
      field_names=['Name','ID Number','Credit Card Number','Credit Card Password','Order Description','Order Amount','Order Time']

      writer=csv.DictWriter(my_file,fieldnames=field_names)
      writer.writeheader()
      writer.writerow(
                {'Name': name, 'ID Number': id, 'Credit Card Number': credit, 'Credit Card Password': password, 'Order Description': total, 
                 'Order Amount': price,'Order Time':now_date})
      order_label.config(text='Your order is preparing...')
      order1_label=Label(second_page,image=order1_image,bg='#F8F4EA')
      order1_label.place(x=150,y=320)
      order2_label=Label(second_page,image=order2_image,bg='#F8F4EA')
      order2_label.place(x=500,y=320)

      



form.mainloop()

