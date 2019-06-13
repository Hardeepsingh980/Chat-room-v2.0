from tkinter import *
from tkinter import messagebox as mb
from csv import DictReader
import temp_csv

def account_func(username):
    f = open('resources/log_details.csv', 'r')
    r = DictReader(f)
    l = []
    for row in r:
        l1 = []
        l1.append(row['name'])
        l1.append(row['username'])
        l1.append(row['password'])
        l1.append(row['avatar'])
        l.append(l1)


    def change_info(arg):
        for i in l:
            if i[0] == username:
                p = i[2]

        if cur_pass.get() == p:
            req = req_pass.get()
            for i in l:
                if i[0] == username:
                    if arg == 'Password':
                        i[2] = req
                    elif arg == 'Name':
                        i[0] = req
                    elif arg == 'Username':
                        i[1] = req
                    elif arg == 'Avatar':
                        i[-1] = req

            ma = ''
            ml = []
            temp = open('resources/temp.txt','w')
            for i in l:
                ml.append(','.join(i))
            to_w = 'name,username,password,avatar'+'@'+'@'.join(ml)
            temp.write(to_w)
            temp.close()
            temp_csv.change()
            name.destroy()

            mb.showinfo('Done',f'{arg} Updated.\n Changes Will Appear Next Time You Open The Application.')
        else:
            mb.showerror('Failed','Password Is Incorrect')

    def change_avatar():

        def set_av(no):
            av.destroy()
            no = str(no)
            f = open('resources/log_details.csv', 'r')
            r = DictReader(f)
            l = []
            for row in r:
                l1 = []
                l1.append(row['name'])
                l1.append(row['username'])
                l1.append(row['password'])
                l1.append(row['avatar'])
                l.append(l1)
            for i in l:
                if i[0] == username:
                    i[-1] = no+'.png'

            ma = ''
            ml = []
            temp = open('resources/temp.txt','w')
            for i in l:
                ml.append(','.join(i))
            to_w = 'name,username,password,avatar'+'@'+'@'.join(ml)
            temp.write(to_w)
            temp.close()
            temp_csv.change()
            mb.showinfo('success','Avatar Changed.')
            pro.destroy()

            


        
        av = Toplevel()
        av.geometry('400x420')
        av.configure(bg='light blue')

        Label(av, text='Choose Avatar',bg='light blue',font=('Calibri Light',20,'bold')).grid(row=0,columnspan=3)

        img_0 = PhotoImage(file='avatars\\0.png')
        Button(av,image=img_0,bg='light blue',bd=0,command=lambda : set_av(0)).grid(row=1,column=0)

        img_1 = PhotoImage(file='avatars\\1.png')
        Button(av,image=img_1,bg='light blue',bd=0,command=lambda : set_av(1)).grid(row=1,column=1)

        img_2 = PhotoImage(file='avatars\\2.png')
        Button(av,image=img_2,bg='light blue',bd=0,command=lambda : set_av(2)).grid(row=1,column=2)

        img_3 = PhotoImage(file='avatars\\3.png')
        Button(av,image=img_3,bg='light blue',bd=0,command=lambda : set_av(3)).grid(row=2,column=0)

        img_4 = PhotoImage(file='avatars\\4.png')
        Button(av,image=img_4,bg='light blue',bd=0,command=lambda : set_av(4)).grid(row=2,column=1)

        img_5 = PhotoImage(file='avatars\\5.png')
        Button(av,image=img_5,bg='light blue',bd=0,command=lambda : set_av(5)).grid(row=2,column=2)

        img_6 = PhotoImage(file='avatars\\6.png')
        Button(av,image=img_6,bg='light blue',bd=0,command=lambda : set_av(6)).grid(row=3,column=0)

        img_7 = PhotoImage(file='avatars\\7.png')
        Button(av,image=img_7,bg='light blue',bd=0,command=lambda : set_av(7)).grid(row=3,column=1)

        img_8 = PhotoImage(file='avatars\\8.png')
        Button(av,image=img_8,bg='light blue',bd=0,command=lambda : set_av(8)).grid(row=3,column=2)

        av.mainloop()

    def del_func():
        res = mb.askquestion('Confirm', 'Are You Sure That You Want To Delete Your Account.',icon='error')
        if res == 'yes':
            c.execute(f'delete from log_details where name = "{username}"')
            db.commit()
        pro.destroy()
        

    def name_func(arg):
        global name
        name = Tk()
        name.geometry('250x200')
        name.title(f'Change {arg}')
        name.configure(bg='light blue')

        Label(name, text=f'Change {arg}',font=('Calibri Light',20,'bold'),bg='light blue').pack()

        Label(name, text='Enter Your Current Password.',font=('Calibri Light',13),bg='light blue').place(x=5,y=40)

        global cur_pass
        cur_pass = Entry(name,font=('Calibri Light',10,'bold'),show='*')
        cur_pass.place(x=5,y=70)

        Label(name, text=f'Enter {arg} You Want To Set.',font=('Calibri Light',13),bg='light blue').place(x=5,y=100)

        global req_pass
        req_pass = Entry(name,font=('Calibri Light',10,'bold'))
        req_pass.place(x=5,y=130)

        Button(name, text='Apply Changes',bd=0,bg='White',fg='black',font=('Calibri Light',10,'bold'),command=lambda:change_info(arg)).place(x=50,y=170)

    
    

    pro = Toplevel()
    pro.geometry('325x425')
    pro.title('Profile')
    pro.configure(bg='light blue')



    f = open('resources/log_details.csv', 'r')
    r = DictReader(f)
    l = []
    for row in r:
        l1 = []
        l1.append(row['name'])
        l1.append(row['username'])
        l1.append(row['password'])
        l1.append(row['avatar'])
        l.append(l1)

    for i in l:
        if i[0] == username:
            if i[-1] == None:
                avar_no = '4.png'
                break
            else:
                avar_no = i[-1]
                break

    avatar = PhotoImage(file=f'avatars\\{avar_no}')

    av_button = Button(pro, image=avatar,bg='light blue',bd=0,command=change_avatar)
    av_button.place(x=110,y=30)

    f = open('resources/log_details.csv', 'r')
    r = DictReader(f)
    l = []
    for row in r:
        l1 = []
        l1.append(row['name'])
        l1.append(row['username'])
        l1.append(row['password'])
        l.append(l1)
    for i in l:
        if i[0] == username:
            user = i[1]
    

    pencil = PhotoImage(file='resources\\pencil-edit-button.png')

    Label(pro,text='@'+user,font=('Calibri Light',16),bg='light blue').place(x=90,y=170)


    Label(pro,text=username.title(),font=('Calibri Light',20,'bold'),bg='light blue').place(x=90,y=140)

    Label(pro, text= 'Change Name',font=('Calibri Light',20),bg='light blue').place(x=10,y=220)

    Button(pro, image=pencil,bg='light blue',bd=0,command=lambda : name_func('Name')).place(x=280,y=220)

    Label(pro, text= 'Change Username',font=('Calibri Light',20),bg='light blue').place(x=10,y=270)

    Button(pro, image=pencil,bg='light blue',bd=0,command=lambda : name_func('Username')).place(x=280,y=270)

    Label(pro, text= 'Change Password',font=('Calibri Light',20),bg='light blue').place(x=10,y=320)

    Button(pro, image=pencil,bg='light blue',bd=0,command=lambda : name_func('Password')).place(x=280,y=320)

    Label(pro, text= 'Delete Account',font=('Calibri Light',20),bg='light blue').place(x=10,y=370)

    delete = PhotoImage(file='resources\\delete.png')

    Button(pro, image=delete,bg='light blue',bd=0,command=del_func).place(x=280,y=370)
    

    pro.mainloop()


#account_func('Hardeep Singh')
