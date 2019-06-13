from tkinter import *
from tkinter import messagebox as mb
import tkinter.scrolledtext as tks
import socket
import _thread
import sys
import account
import pygame
from csv import DictReader

pygame.mixer.init()


def main_func(username):

    i = 3
    client = 0
    start = True

    client_name = []
    client_name.append(username)        
  
        

    def del_dups(l):
        dup = []
        for i in l:
            if i not in dup:
                dup.append(i)
            else:
                pass
        global client_name
        client_name = dup
        return dup


    
    def log_out(username):
        to = username +',gone980'
        c.send(to.encode('ascii'))
        win.destroy()

        


    def list_insert(msg):
        active_users.delete(0,END)


        

        global active_list
        active_list = []
                
        for i in range(0,len(msg)):
            m = msg[i].split(',')
            for j in range(0,len(m)):
                client_name.append(m[j])
                active_users.insert(i+1,m[j])

                                    
        
    
    def sendMessage (username,*args):
        u = username.split()[0]
        msg = u + ' : '+msg_entry.get()
        global c
        c.send(msg.encode('ascii'))

    def recievingMessage (c): 
        while True :
            msg=c.recv(2048).decode('ascii')
            if 'new980' in msg:
                msg = msg.split('@')
                msg.pop(-1)
                list_insert(msg)
                for i in msg:
                    client_name.append(i)
                pygame.mixer.music.load('resources\\new_user.mp3')
                pygame.mixer.music.play()
                

            elif 'gone980' in msg:
                msg = msg.split('@')
                msg.pop(-1)
                list_insert(msg)
                for i in msg:
                    client_name.append(i)
                pygame.mixer.music.load('resources\\log_out.mp3')
                pygame.mixer.music.play()

            else:
                t = text.get(1.0,END)
                text.delete(1.0,END)
                text.insert(INSERT,t+msg+'\n')
                text.yview('end')
                pygame.mixer.music.load('resources\\recv_message.mp3')
                pygame.mixer.music.play()





            
    #Socket Creation
    def socketCreation (username):
        global c
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        host = '127.0.0.1'
        port = 5000
        c.connect((host,port))
        msg = username + ',new980'
        c.send(msg.encode('ascii'))
        global client
        client = c
        _thread.start_new_thread(recievingMessage, (c,) )




    win = Toplevel()
    win.geometry('530x400')
    win.resizable(0,0)
    win.title(f'Chat\{username}')

    Label(win, text='Chat',bg='white', font=('arial black',13),width=50,height=1).pack()

    
    
    text = tks.ScrolledText(win,height=17,width=41, font=('arial black',10),wrap=WORD)
    text.place(x=10,y=40)
    text.yview('end')

    


    msg_entry = Entry(win, font=('arial black',13),width=25)
    msg_entry.place(x=10,y=365)

    send = Button(win, font=('arial black',10), text='Send',bd=0,bg='blue',fg='white',width=10,command=lambda : sendMessage(username))
    send.place(x=300,y=365)

    Label(win, font=('arial black',13),bg='blue',fg='white',text='Users',width=12).place(y=40,x=400)

    f = open('resources/log_details.csv', 'r')
    r = DictReader(f)
    l = []
    for row in r:
            l1 = []
            l1.append(row['name'])
            l.append(l1)

    user_list = Listbox(win,height=8,width=20)
    user_list.place(x=400,y=70)
    for i in l:        
        user_list.insert(END,i[0])



    

    Label(win, font=('arial black',13),bg='Green',fg='white',text='Active Users',width=10).place(y=200,x=400)

    active_users = Listbox(win,height=8,width=20)
    active_users.place(x=400,y=230)

    Label(win, text='Logged In as : \n'+ username,font=('arial black',10)).place(x=400,y=360)

    global set_img
    set_img = PhotoImage(file='resources\\icons8-menu-48.png')
    set_img = set_img.subsample(2)
    
    menu_b = Button(win, image=set_img,bd=0,bg='white')
    menu_b.image = set_img
    menu_b.place(x=490,y=2)

    

    def clear_chat_func():
        text.delete(1.0,END)


    pop = Menu(win, tearoff=0)    
    pop.add_command(label='Account Settings',command=lambda:account.account_func(username))
    pop.add_separator()
    pop.add_command(label='Clear Chat',command=clear_chat_func)
    pop.add_separator()
    pop.add_command(label='Log Out',command=lambda: log_out(username))

    def do(event):
        try:
            pop.tk_popup(event.x_root,event.y_root,0)
        finally:
            pop.grab_release


    menu_b.bind('<Button-1>',do)



    def key_press(*args):
        sendMessage(username)
    
    win.bind('<Return>',key_press)

    _thread.start_new_thread(socketCreation, (username,) )
    



    win.mainloop()






###Creating a window
##window = tkinter.Tk()
##window.title('Client')
##window['bg']='gray98'
##window['padx']=10
##window['pady']=10
###Adding Elements
###Entry
##txt = tkinter.Entry(window)
##txt['width']=60
##txt['relief']=tkinter.GROOVE
##txt['bg']='white'
##txt['fg']='green'
##txt['font']=("",18)
##txt.grid(column=0,row=1,padx=5,pady=15)
###Button
##send = tkinter.Button(window,text="send")
##send['relief']=tkinter.GROOVE
##send['bg']='white'
##send['fg']='green'
##send['activebackground']='ivory3'
##send['padx']=3
##send['font']=("",18)
##send.grid(column=1,row=1,padx=5,pady=15)
###Lable
##lbl = tkinter.Label(window,text='Starting Chat Application')
##lbl['font']=("",18)
##lbl['bg']='white'
##lbl['width']=62
##lbl.grid(columnspan=2,column=0,row=2,padx=5)

##
##
##window.mainloop()

#main_func('Hardeep Singh')





