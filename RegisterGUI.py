from tkinter import *
import tkinter.font as font
import mysql.connector

con = mysql.connector.connect(host="localhost",username="root",password="root",database="loginDB")
cursordb = con.cursor()

def login():
    u = user.get()
    p = pswd.get()
    sql = "select * from users where username = %s and password = %s"
    cursordb.execute(sql,[(u),(p)])
    results = cursordb.fetchall()
    if(u != "" and p != ""):
        if len(results) == 0:
            errorMsg = Label(login_Frame,text="Incorrect username or password",font=font_label,fg="red")
            errorMsg.pack()
            errorMsg.place(x=35,y=500)
        else:
            for i in results:
                home_Window()
                break    

def create():
    nuser = newuser.get()
    npswd = newpswd.get()
    q = "insert into users(username,password) values ('%s','%s')" % (nuser,npswd)
    if(nuser == "" and npswd == ""):
        emptyMsg = Label(signUp_Frame,text="Fields cannot be empty",font=font_label,fg="red")
        emptyMsg.pack()
        emptyMsg.place(x=40,y=500)
    else:
        cursordb.execute(q)
        con.commit() 
        successMsg = Label(signUp_Frame,text="Account has been created succsessfully",font =font.Font(family="Poppins",size=10),fg="red")
        successMsg.pack()
        successMsg.place(x=35,y=500)  

def register_Window():
    global newuser
    global newpswd
    newuser = StringVar()
    newpswd = StringVar()
    titleLabel = Label(signUp_Frame,text="CREATE",font=font_title)
    userLabel = Label(signUp_Frame,text="Enter username",font=font_label)
    pwdLabel = Label(signUp_Frame,text="Enter password",font=font_label)

    userInput = Entry(signUp_Frame,textvariable=newuser,borderwidth=0,bg="#ccc")
    pswdInput = Entry(signUp_Frame,textvariable=newpswd,borderwidth=0,bg="#ccc")

    createBtn = Button(signUp_Frame, image=createBtnImg,borderwidth=0,command=create)
    alreadyBtn = Button(signUp_Frame,text="Already have an account",borderwidth=0,font=font_small,command=login_Window)

    # packing
    titleLabel.pack()
    userLabel.pack()
    userInput.pack()
    pwdLabel.pack()
    pswdInput.pack()
    createBtn.pack()
    alreadyBtn.pack()

    # placing
    titleLabel.place(x=100,y=140)
    userLabel.place(x=43,y=240)
    userInput.place(x=43,y=280,width=273,height=33)
    pwdLabel.place(x=43,y=320)
    pswdInput.place(x=43,y=360,width=273,height=33)
    createBtn.place(x=35,y=555)
    alreadyBtn.place(x=100,y=400)


    signUp_Frame.pack(fill="both",expand=1)
    login_Frame.forget()

def login_Window():
    # Adding widgets to login frame
    global user
    global pswd
    user = StringVar()
    pswd = StringVar()
    titleLabel = Label(login_Frame,text="LOGIN",font=font_title)
    userLabel = Label(login_Frame,text="Enter username",font=font_label)
    pwdLabel = Label(login_Frame,text="Enter password",font=font_label)

    # Entry widgets of login frame
    userInput = Entry(login_Frame,textvariable=user,borderwidth=0,bg="#ccc")
    pswdInput = Entry(login_Frame,textvariable=pswd,borderwidth=0,bg="#ccc",show="*")

    loginBtn = Button(login_Frame, image=loginBtnImg,borderwidth=0,command=login)
    registerBtn = Button(login_Frame,text="Create a new account",borderwidth=0,font=font_small,command=register_Window)

    # packing
    titleLabel.pack()
    userLabel.pack()
    userInput.pack()
    pwdLabel.pack()
    pswdInput.pack()
    loginBtn.pack()
    registerBtn.pack()

    # placing
    titleLabel.place(x=120,y=140)
    userLabel.place(x=43,y=240)
    userInput.place(x=43,y=280,width=273,height=33)
    pwdLabel.place(x=43,y=320)
    pswdInput.place(x=43,y=360,width=273,height=33)
    loginBtn.place(x=35,y=555)
    registerBtn.place(x=100,y=400)

    login_Frame.pack(fill="both",expand=1)
    signUp_Frame.forget()
    home_Frame.forget()

def home_Window():
    greeting = Label(home_Frame,text="Welcome : {}".format(user.get()),font=font_label,bg="#c2f8cb")
    Label(home_Frame,image=welcomeImg,width=300).pack()
    greeting.pack()
    logoutBtn = Button(home_Frame,text="LOGOUT",bg="#F78E8E",borderwidth=0,command=login_Window)
    logoutBtn.pack()
    logoutBtn.place(x=150,y=500)
    home_Frame.pack(fill="both",expand=1)
    login_Frame.forget()

# Main root frame 
mainFrame = Tk()
mainFrame.title("Login form")
mainFrame.iconphoto(True,PhotoImage(file="G:\\BCA\\TY\\1st_Sem\\Python\\Program\\Assignments\\Project\\GUI\\logo.png"))

# centering the window
width,height = 360,640
s_width = mainFrame.winfo_screenwidth()
s_height = mainFrame.winfo_screenheight()
x_cord = int((s_width / 2) - (width / 2))
y_cord = int((s_height / 2) - (height / 2))
mainFrame.geometry("{}x{}+{}+{}".format(width,height,x_cord,y_cord))

# three frames
login_Frame = Frame(mainFrame)
signUp_Frame = Frame(mainFrame)
home_Frame = Frame(mainFrame)

# font property
font_label = font.Font(family="Poppins",size=16)
font_title = font.Font(family="Geometos",size=30)
font_small = font.Font(family="Poppins",size=12)

#  image urls
loginBtnImg = PhotoImage(file="G:\\BCA\\TY\\1st_Sem\\Python\\Program\\Assignments\\Project\\GUI\\signInBtn.png")
createBtnImg = PhotoImage(file="G:\\BCA\\TY\\1st_Sem\\Python\\Program\\Assignments\\Project\\GUI\\createBtn.png")
welcomeImg = PhotoImage(file="G:\\BCA\\TY\\1st_Sem\\Python\\Program\\Assignments\\Project\\GUI\\avatar.png")
login_Window()
mainloop()
