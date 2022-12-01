from tkinter import *
from tkinter import messagebox
import ast


#Log-in GUI
root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

#Sign In Instructions
def signin():
    username=user.get()
    password=enter.get()

    #Opens and reads text file as dictionary
    file = open("accounts.txt", "r")
    d= file.read()
    r=ast.literal_eval(d)
    file.close()


    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        Label(screen,text="Hello Everyone!", bg="#fff", font=("Calibri(Body",50,"bold")).pack(expand=True)
        screen.mainloop()
    else:
        messagebox.showerror("Invalid", "Invalid username or password")

#Sign Up GUI system
def createAccount():
    #Sign Up interface
    window=Toplevel(root)
    window.title("Sign Up")
    window.geometry('925x500+300+200')
    window.configure(bg="#fff")
    window.resizable(False, False)


    #Pending Logo
    #img = PhotoImage(file='login.png')
    #Label(window, image=img, border = 0, bg= "white").place(x=50, y=90)

    frame= Frame(window, width=350, height=390, bg="#fff")
    frame.place(x=480,y=50)

    heading= Label(frame, text='Sign up', fg="#57a1f8", bg = "white",font=("Microsoft YaHei UI Light",23,"bold"))
    heading.place(x=100,y=5)

    #Sign Up system
    def signup():
        username= user.get()
        password= access.get()
        confirm_pass = confirm.get()

        file=open("accounts.txt", "r")
        data = file.readline()
        if len(password) < 8:
            messagebox.showerror("Invalid", "You need at least 8 characters in your password")
        else:    
            try:
                r = ast.literal_eval(data)
                d = r.keys()
            except:
                file.close()
            if password == confirm_pass:
                if username not in d:
                    file.close()
                    try:
                        file=open("accounts.txt", "r+")
                        d =file.read()
                        r=ast.literal_eval(d)

                        dict2={username:password}
                        r.update(dict2)
                        file.truncate(0)
                        file.close()

                        file=open("accounts.txt", "w")
                        w = file.write(str(r))
                        messagebox.showinfo("Signup", "Successfully created your account")
                    except:
                        file=open('accounts.txt', "w")
                        pp = str({username:password})
                        file.write(pp)
                        file.close()
                        messagebox.showinfo("Signup", "Successfully Created your account")    
                else:
                    messagebox.showerror("Invalid", "There is an existing account with this username")
            else:
                messagebox.showerror("Invalid", "Both passwords should match")

    def signin():
        window.destroy()

    #Username Input
    def on_enter(x):
        user.delete(0, "end")
    def on_leave(x):
        if user.get()=="":
            user.insert(0,"Username")
    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)

    #Password Input
    def on_enter(x):
        access.delete(0, "end")
    def on_leave(x):
        if access.get()=="":
            access.insert(0,"Password")
    access = Entry(frame, width=25, fg="black", border =0, bg="white", font=("Microsoft YaHei UI Light", 11))
    access.place(x=30, y=150)
    access.insert(0, "Password")
    access.bind("<FocusIn>", on_enter)
    access.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25,y=177)

    #Confirm Password Input
    def on_enter(x):
        confirm.delete(0, "end")
    def on_leave(x):
        if access.get()=="":
            confirm.insert(0,"Confirm Password")
    confirm = Entry(frame, width=25, fg="black", border =0, bg="white", font=("Microsoft YaHei UI Light", 11))
    confirm.place(x=30, y=220)
    confirm.insert(0, "Confirm Password")
    confirm.bind("<FocusIn>", on_enter)
    confirm.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25,y=247)


    #Return to Login
    Button(frame,width=39,pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0, command= signup).place(x=25,y=274)
    label=Label(frame,text="I have an account", fg="black",bg="white", font=("Microsoft YaHei UI Light", 9))
    label.place(x=75, y=340)

    signin= Button(frame, width=6, text="Sign In", border = 0, bg= "white", cursor='hand2', fg="#57a1f8", command= signin)
    signin.place(x=200, y=340)

    window.mainloop()
    root.destroy()
#Image
#img = PhotoImage(file='login.png')
#Label(root, image=img,bg="white").place(x=50, y=50)


frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480,y=70)

heading = Label(frame, text="Sign in", fg='#57a1f8', border = 0, bg="white", font=('Microsoft YaHei UI Light', 23, "bold"))
heading.place(x=100, y= 5)

#Login Input
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name =="":
        user.insert(0, "Username")
user = Entry(frame, width=25, fg='black', border =0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25,y=107)

#Password Input
def on_enter(e):
    enter.delete(0, 'end')
def on_leave(e):
    user=enter.get()
    if enter =="":
        user.insert(0, "Username")
enter = Entry(frame, width=25, fg='black', border =0, bg="white", font=("Microsoft YaHei UI Light", 11))
enter.place(x=30, y=150)
enter.insert(0, "Password")
enter.bind("<FocusIn>", on_enter)
enter.bind("<FocusOut>", on_leave)

Frame(frame,width=295, height=2, bg="black").place(x=25,y=177)

Button(frame,width=39,pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command= signin).place(x=25,y=204)
label=Label(frame,text="Don't have an account?", fg="black",bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)

signup = Button(frame, width=6, text= "Sign up", border=0, bg='white',cursor="hand2", fg="#57a1f8", command = createAccount)
signup.place(x=215,y=270)

root.mainloop()