from tkinter import*
from tkinter import messagebox
import pickle
import math
import datetime

root = Tk()
root.geometry("300x500")
root.title("Войти в систему")
root.configure(background="#393531")


def chek_btn_reg(i=[0]):
    i[0]+=1
    if i[0]<2:
        login()
    return i[0]

def chek_btn(i=[0]):
    i[0]+=1
    if i[0]<2:
        choise()
    return i[0]


def clock11():
    root3=Tk()
    root3.title("clock")
    root3.configure(background="#393531")

    def x_coordinate(lenght,angle):
        return width/2+lenght*math.cos(angle*math.pi/180)

    def y_coordinate(lenght,angle):
        return height /2-lenght*math.sin(angle*math.pi/180)

    width = 400
    height = 400
    radius=150

    canvas=Canvas(root3,height=height,width=width,background="#393531")
    canvas.pack()

    canvas.create_oval(width/2-radius, height/2-radius, width/2+radius, height/2+radius)
    seconds=canvas.create_line(0,0,0,0,fill="red")
    minutes=canvas.create_line(0,0,0,0,fill="white")
    hours=canvas.create_line(0,0,0,0,fill="white")


    def change_hand(lenght,time,clock_hand,degree):
        alpha=90-time*degree
        x1=x_coordinate(0,alpha)
        y1=y_coordinate(0,alpha)
        x2=x_coordinate(lenght, alpha)
        y2=y_coordinate(lenght, alpha)
        canvas.coords(clock_hand,x1,y1,x2,y2)
        canvas.pack()


    def update():
        time=str(datetime.datetime.now())
        sec= int(time [17:19])
        minu=int(time[14:16])
        h=int(time[11:13])

        change_hand(radius-20,sec,seconds,6)
        change_hand(radius-40,minu,minutes,6)
        change_hand(radius/2,h,hours,6)
        root3.after(1000,update)
    alpha=60

    for i in range(1,13):
        canvas.create_text(x_coordinate(radius+18,alpha),y_coordinate(radius+18,alpha),text=i,fill='white',font="Times 10  bold")
        alpha=alpha-30
    for i in range(60):
        x1=x_coordinate(radius,alpha)
        y1=y_coordinate(radius,alpha)
        if alpha%30==0:
            x2=x_coordinate(radius-20,alpha)
            y2=y_coordinate(radius-20,alpha)
        else:
            x2=x_coordinate(radius-10,alpha)
            y2=y_coordinate(radius-10,alpha)
        canvas.create_line(x1,y1,x2,y2)
        alpha+=6

    update()

    root3.mainloop()


def sinusoida():
    root1=Tk()
    root1.title("Построение графика функции")
    root1.geometry("1320x640" )
    root1.configure(background="#393531")

    canvas=Canvas(root1,width=1040,height=640,bg="#393531")
    canvas.pack()

    for y in range(21):
     k= 50 * y
     canvas.create_line(20+k,620,20+k,20,width=1,fill='#000')

    for x in range(13):
     k= 50 * x
     canvas.create_line(20,20+k,1020,20+k,width=1,fill='#000')

    canvas.create_line(20,20,20,620,width=1,arrow=FIRST,fill='white')
    canvas.create_line(10,320,1020,320,width=1,arrow=LAST,fill='white')

    canvas.create_text(20,10,text='300',fill="white")
    canvas.create_text(20,630,text='-300',fill="white")
    canvas.create_text(10,310,text='0',fill="white")
    canvas.create_text(1030,310,text='1000',fill="white")

    label_w=Label(root1,text='циклическая чистота:',background="#393531",fg='white')
    label_w.place(x=0,y=10)
    label_phi=Label(root1,text='смещение графика по X:',background="#393531",fg='white')
    label_phi.place(x=0,y=30)
    label_A=Label(root1,text='Амплитуда:',background="#393531",fg='white')
    label_A.place(x=0,y=50)
    label_dy=Label(root1,text='Смещение графика по Y:',background="#393531",fg='white')
    label_dy.place(x=0,y=70)

    entry_w=Entry(root1)
    entry_w.place(x=150, y=10)
    entry_phi=Entry(root1)
    entry_phi.place(x=150, y=30)
    entry_A=Entry(root1)
    entry_A.place(x=150, y=50)
    entry_dy=Entry(root1)
    entry_dy.place(x=150, y=70)


    def sinus(W, phi, A, dy):
        global sin
        sin=0
        xy=[]
        for x in range(1000):
            y = math.sin(x * W)
            xy.append(x + phi)
            xy.append(y * A +  dy)
        sin = canvas.create_line(xy,fill="white")


    def clean():
        canvas.delete(sin)

    btn_calc=Button(root1, text='Расчитать')
    btn_calc.bind('<Button-1>',lambda event : sinus(float(entry_w.get()),
                                                    float(entry_phi.get()),
                                                    float(entry_A.get()),
                                                    float(entry_dy.get())))

    btn_calc.place(x=10,y=100)

    btn_clean=Button(root1,text='Очистить')
    btn_clean.bind('<Button-1>',lambda event:clean())
    btn_clean.place(x=100,y=100)

    canvas.pack(side='right')

    root1.mainloop()


def regestration():
    text=Label(text="Для входа в систему зарегистрируйтесь!",fg='white',background="#393531",font="calibri")
    text_log=Label(text="Введите ваш логин:",font="cambria",background="#393531",fg='white')
    reg_log=Entry()
    text_pass=Label(text="Введите ваш пароль:",background="#393531",fg='white',font="cambria")
    reg_pass=Entry()
    btn_reg=Button(text="Зарегестрироваться",background="Green",fg='white',font="calibri",command=lambda:save())

    text.pack()
    text_log.pack()
    reg_log.pack()
    text_pass.pack()
    reg_pass.pack()
    btn_reg.pack()

    def save():
        login_pass_save={}
        login_pass_save[reg_log.get()]=reg_pass.get()
        f=open('login.txt','wb')
        pickle.dump(login_pass_save,f)
        f.close()
        chek_btn_reg()


def choise():
    btn_choise=Button(root, text='Sin',width=5,height=3,background="orange",fg='white',font="cambria")
    btn_choise.bind('<Button-1>',lambda event : sinusoida())
    btn_choise.pack()

    btn_choise_1=Button(root, text='Clock',width=5,height=3,background="orange",fg='white',font="cambria")
    btn_choise_1.bind('<Button-1>',lambda event :clock11())
    btn_choise_1.pack()


def login():
    text_loggin=Label(text="Можете войти в систему!",font="cambria ",background="#393531",fg='white')
    text_enter_login=Label(text="Введите ваш логин:",background="#393531",font="cambria",fg='white')
    enter_login=Entry()
    text_enter_pass=Label(text="Введитеваш пароль:",background="#393531",font="cambria",fg='white')
    enter_password=Entry(show='*')
    button_enter=Button(text="Войти",command=lambda:log_pass(),background="green",font="cambria",fg='white')

    text_loggin.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_enter.pack()


    def log_pass():
        f=open("login.txt",'rb')
        a=pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get()==a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен","Вы получили доступ к расчету синусойды и часам")
                chek_btn()
            else:
                messagebox.showerror("Ошибка входа","Вы ввели неверный логин либо пароль")
        else:
             messagebox.showerror("Ошибка!","Ошибка!")


regestration()
root.mainloop()
