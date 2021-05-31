from tkinter import *

root = Tk()
root.geometry('500x300')
bg = PhotoImage( file = "study focus.png")
root.title("study focus")
Labelbg= Label(root,image=bg)
Labelbg.place(x=0,y=0)
host_path ='/etc/hosts'
redirect = '127.0.0.1'  
Label(root, text ='Enter Website :' , font ='arial 13 bold').place(x=30,y=95)
Websites = Text(root,font = 'arial 10',height='1.5', width = '40')
Websites.place(x= 160,y = 95)

def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    if block : 
        with open (host_path , 'r+') as host_file:
            file_content = host_file.read()
            for web in Website: 
                if web in file_content:
                    Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=250)
                    
                    pass
                else:
                    host_file.write(redirect+ " " + web + '\n')      
                    Label(root, text = "Blocked", font = 'arial 12 bold').place(x=200,y =250)  
                    
def Unblocker() :  
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))          
    if unblock:
        with open(host_path, 'r+') as host_file:
            lines  = host_file.readlines() 
            host_file.seek(0)       
            for line  in lines:
                if not any(site in line for site in Website):
                    host_file.write(line)
            host_file.truncate()
            Label(root, text = "Unblocked", font = 'arial 12 bold').place(x=200,y =250)
            


block = Button(root, text = 'Block',font = 'arial 12 bold',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')
block.place(x = 250, y = 150)

unblock = Button(root, text = 'Unblock',font = 'arial 12 bold',pady = 5,command = Unblocker ,width = 7, bg = 'royal blue1', activebackground = 'sky blue')
unblock.place(x = 245, y = 200)



root.mainloop() 