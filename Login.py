import tkinter
from tkinter import messagebox
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Sudha@123")
global cur
cur=con.cursor()
try:
    cur.execute('use credential')
except:
    cur.execute('create database credential')
    cur.execute('use credential')
    cur.execute('create table login (user_id varchar(20),password varchar(20))')
def check():
    con=mysql.connector.connect(host="localhost",user="root",password="Sudha@123")
    cur=con.cursor()
    cur.execute('use credential')
    cur.execute(f'select count(password) from login where user_id="{e1.get()}" and password="{e2.get()}"')
    if cur.fetchall():
        t_obj.destroy()
        import Main
    else:
        messagebox.askretrycancel('Warning','Wrong user name or password')
    con.commit()
    con.close()
def insert():
    con=mysql.connector.connect(host="localhost",user="root",password="Sudha@123")
    cur=con.cursor()
    cur.execute('use credential')
    cur.execute(f"insert into login values ('{e1.get()}','{e2.get()}')")
    messagebox.showinfo('Created','login created successfully' )
    con.commit()
    con.close()
con.commit()
con.close()
t_obj=tkinter.Tk()
t_obj.geometry('250x150')
t_obj.title('Registraion Page') 
l1=tkinter.Label(t_obj,text='User Name :')
l2=tkinter.Label(t_obj,text='Password :')
l1.grid(row=2,column=2)
l2.grid(row=4,column=2)
e1=tkinter.Entry(t_obj)
e2=tkinter.Entry(t_obj)
e1.grid(row=2, column=4)
e2.grid(row=4,column=4)
b1=tkinter.Button(t_obj,text='Log in',command=check)
b2=tkinter.Button(t_obj,text='Sign up',command=insert)
b1.grid(row=6,column=2)
b2.grid(row=6,column=4)
t_obj.mainloop()