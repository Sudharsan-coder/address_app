from tkinter import *
import mysql.connector

def add():  
    con=mysql.connector.connect(host="localhost",user="root",password="Sudha@123")
    cur=con.cursor()
    cur.execute("use credential")
    cur.execute(f"insert into address values('{Name.get()}',{Number.get()},'{address.get()}')")
    con.commit()
    con.close()
    l.config(text='Inserted successfully')

def delete():
    con=mysql.connector.connect(host="localhost",user="root",password="Sudha@123")
    cur=con.cursor()
    cur.execute("use credential")
    try:
        cur.execute(f"delete from address where name='{Name.get()}' and number={Number.get()} and addre='{address.get()}'")
    except:
        l.config(text="There is no previous address exist")
        return 
    con.commit()
    con.close()
    l.config(text='deleted successfully')


def display():
    #import display
    root1=Toplevel(root)
    root1.geometry('500x500')
    root1.title('Display')
    con=mysql.connector.connect(host='localhost',user='root',password='Sudha@123',database='credential')
    cur=con.cursor()
    cur.execute('select * from address')
    res=cur.fetchall()
   
    s=1
    for i in res:
        Label(root1,text=str(s)+'.   '+i[0]+'    ').place(x=80,y=gap)
        Label(root1,text=i[1]).place(x=180,y=gap)
        Label(root1,text=i[2]).place(x=310,y=gap)
        gap+=50
        s+=1
root = Tk()
root.geometry('500x500')

Name = StringVar()
Number = StringVar()
address=StringVar()

main_menu=Menu(root)
main_menu.add_command(label='Display',command=display)
main_menu.add_command(label='|')
main_menu.add_command(label='Exit',command=root.quit)
root.config(menu=main_menu)



Label(root, text = 'Name').place(x=10,y=10)
Entry(root, textvariable = Name,width=50).place(x=100,y=10)

Label(root, text = 'Phone No.').place(x=10,y=50)
Entry(root, textvariable = Number,width=50).place(x=100,y=50)

Label(root, text = 'Address').place(x=10,y=90)
Entry(root,textvariable=address,width=55).place(x=100,y=90)

Button(root,text="Add",command=add).place(x=10,y=130)
Button(root,text="Delete",command=delete).place(x=90,y=130)


l=Label(root)
l.place(x=10,y=200)
root.mainloop()