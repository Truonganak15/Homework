#!/usr/bin/env python
# coding: utf-8

# In[6]:


# nhap vao cac thu vien

from tkinter import *
from tkinter import messagebox
import tempfile
import os
import tkinter.ttk as ttk
import openpyxl

# set up cua so ung dung

root=Tk()
root.title('Billing Management System')
root.geometry('1280x720')
bg_color='gray'

#Khai bao cac bien
#=====================variables===================
Beef=IntVar()
Wine=IntVar()
Rice=IntVar()
Milk=IntVar()
Total=IntVar()

cb=StringVar()
cw=StringVar()
cr=StringVar()
cm=StringVar()
total_cost=StringVar()

# khai bao ham
# ===========Function===============



def total():
    if Beef.get()==0 and Wine.get()==0 and Rice.get()==0 and Milk.get()==0:
        messagebox.showerror('Error','Please select quantity')
    else:
        b=Beef.get()
        w=Wine.get()
        r=Rice.get()
        m=Milk.get()

        t=float(b*10+w*9+r*8+m*7)
        Total.set(b + w + r + m)
        total_cost.set('$ ' + str(round(t, 0)))

        cb.set('$ '+str(round(b * 10, 2)))
        cw.set('$ '+str(round(w*9,2)))
        cr.set('$ '+str(round(r*8,2)))
        cm.set('$ '+str(round(m*7,2)))
    
def cal_price(input):
    output = int(input.replace("$", ""))
    return output
        
def save_receipt():
    b= Beef.get()
    ccb= cb.get()
    w= Wine.get()
    ccw= cw.get()
    r = Rice.get()
    ccr= cr.get()
    m = Milk.get()
    ccm= cm.get()
    
    
    ccb = cal_price(ccb)
    ccw = cal_price(ccw)
    ccr = cal_price(ccr)
    ccm = cal_price(ccm)
    
    t= b+w+r+m
    cct = ccb+ccw+ccr+ccm
    
    filepath = r"C:\Users\Son Nguyen\Desktop\chanqua.xlsx"
    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ["Beef", "Beef cost", "Wine","Wine cost","Rice", "Rice cost", "Milk", "Milk cost", "Total", "Total cost($)"]
        sheet.append(heading)
        workbook.save(filepath)
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([b, ccb, w, ccw, r, ccr,m, ccm, t, cct])
    workbook.save(filepath) 

def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,' Items\tNumber of Items\t  Cost of Items\n')
    textarea.insert(END,f'\nPayment\t\t{ptype_txt.get()}')
    textarea.insert(END,f'\nBeef\t\t{Beef.get()}\t  {cb.get()}')
    textarea.insert(END,f'\n\nWine\t\t{Wine.get()}\t  {cw.get()}')
    textarea.insert(END,f'\n\nRice\t\t{Rice.get()}\t  {cr.get()}')
    textarea.insert(END,f'\n\nMilk\t\t{Milk.get()}\t  {cm.get()}')
    textarea.insert(END, f"\n\n================================")
    textarea.insert(END,f'\nTotal Price\t\t{Total.get()}\t{total_cost.get()}')
    textarea.insert(END, f"\n================================")


def print():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open(filename,'w').write(q)
    os.startfile(filename,'Print')


def reset():
    textarea.delete(1.0,END)
    Beef.set(0)
    Wine.set(0)
    Rice.set(0)
    Milk.set(0)
    Total.set(0)
    btype_txt.set('')

    cb.set('')
    cw.set('')
    cr.set('')
    cm.set('')
    total_cost.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()

title=Label(root, pady=5, text="Billing Management System",bd=12,bg=bg_color,fg='white',font=('times new roman', 35 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#===============Product Details=================

F1 = LabelFrame(root, text='DETAILS', font=('times new roman', 18, 'bold'), fg='gold',bg=bg_color,bd=15,relief=RIDGE)
F1.place(x=5, y=90,width=800,height=600)

#=====================Heading==========================
itm=Label(F1, text='Items', font=('Helvetic',25, 'bold','underline'), fg='white',bg=bg_color)
itm.grid(row=1,column=0,padx=20,pady=15)

n=Label(F1, text='Number of Items', font=('Helvetic',25, 'bold','underline'), fg='white',bg=bg_color)
n.grid(row=1,column=1,padx=30,pady=15)

cost=Label(F1, text='Cost of Items', font=('Helvetic',25, 'bold','underline'), fg='white',bg=bg_color)
cost.grid(row=1,column=2,padx=30,pady=15)

#===============Product============

paymenttype=Label(F1, text='Payment', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
paymenttype.grid(row=0,column=0,padx=20,pady=15)
ptype_txt=ttk.Combobox(F1, font='arial 15 bold')
ptype_txt["values"] = ("Cash", "Bank Transfer", "Credit Card")
ptype_txt.grid(row=0,column=1,padx=20,pady=15)


beef=Label(F1, text='Beef', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
beef.grid(row=2,column=0,padx=20,pady=15)
b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Beef,justify=CENTER)
b_txt.grid(row=2,column=1,padx=20,pady=15)
cb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cb,justify=CENTER)
cb_txt.grid(row=2, column=2,padx=20,pady=15)

wine=Label(F1, text='Wine', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
wine.grid(row=3,column=0,padx=20,pady=15)
w_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Wine,justify=CENTER)
w_txt.grid(row=3,column=1,padx=20,pady=15)
cw_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cw,justify=CENTER)
cw_txt.grid(row=3,column=2,padx=20,pady=15)

rice=Label(F1, text='Rice', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
rice.grid(row=4,column=0,padx=20,pady=15)
r_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Rice,justify=CENTER)
r_txt.grid(row=4,column=1,padx=20,pady=15)
cr_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cr,justify=CENTER)
cr_txt.grid(row=4,column=2,padx=20,pady=15)

milk=Label(F1, text='Milk', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
milk.grid(row=5,column=0,padx=20,pady=15)
m_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Milk,justify=CENTER)
m_txt.grid(row=5,column=1,padx=20,pady=15)
cm_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cm,justify=CENTER)
cm_txt.grid(row=5,column=2,padx=20,pady=15)

t=Label(F1, text='TOTAL', font=('times new rommon',20, 'bold'), fg='red',bg=bg_color)
t.grid(row=6,column=0,padx=20,pady=15)
t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Total,justify=CENTER, fg = 'red')
t_txt.grid(row=6,column=1,padx=20,pady=15)
totalcost_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=total_cost,justify=CENTER, fg = 'red')
totalcost_txt.grid(row=6,column=2,padx=20,pady=15)

#=====================Bill area====================
F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=90,width=430,height=500)
bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F2,orient=VERTICAL)
scrol_y.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol_y.set)
textarea.pack(fill=BOTH)
scrol_y.config(command=textarea.yview)



#=====================Buttons========================
F3 =Frame(root,bg=bg_color,bd=15,relief=RIDGE)
F3.place(x=5, y=590,width=1270,height=120)

btn1 = Button(F3, text='Total', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=8,command=total)
btn1.grid(row=0,column=0,padx=20,pady=10)

btn2 = Button(F3, text='Receipt', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=8,command=receipt)
btn2.grid(row=0,column=1,padx=10,pady=10)

btn3 = Button(F3, text='Print', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=8,command=print)
btn3.grid(row=0,column=2,padx=10,pady=10)

btn4 = Button(F3, text='Reset', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=8,command=reset)
btn4.grid(row=0,column=3,padx=10,pady=10)

btn5 = Button(F3, text='Exit', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=8,command=exit)
btn5.grid(row=0,column=5,padx=10,pady=10)

btn5 = Button(F3, text='Save', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=8,command=save_receipt)
btn5.grid(row=0,column=4,padx=10,pady=10)





root.mainloop()





# In[ ]:





