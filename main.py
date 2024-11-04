import smtplib
from email.message import EmailMessage
from tkinter import *


def send_email():
    sender='python-sony@yandex.ru'
    recipient='sofico86solo@yandex.ru'
    password='jhswqwovscdzxiul'
    tema='Проверка связи'
    body='Привет из программы на Питоне!'

    msg=EmailMessage()
    msg.set_content(body)
    msg['Subject']=tema
    msg['From']=sender
    msg['To']=recipient
    server=None
    try:
        server=smtplib.SMTP_SSL('smtp.yandex.ru',465)
        server.login(sender,password)
        server.send_message(msg)
        print("Письмо отправлено!")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if server:
            server.quit()

win=Tk()
win.title("Отправка е-майл")
win.geometry("500x300")

Label(text="Отправитель: ".grid(row=0,column=0,sticky=W))
send_email=Entry()
send_email.grid(row=0,column=1,sticky=W)

Label(text="Получатель: ".grid(row=1,column=0,sticky=W))
recip_email=Entry()
recip_email.grid(row=1,column=1,sticky=W)

Label(text="Пароль приложения: ".grid(row=2,column=0,sticky=W))
password=Entry()
password.grid(row=2,column=1,sticky=W)

Label(text="Тема письма: ".grid(row=3,column=0,sticky=W))
tema=Entry()
tema.grid(row=3,column=1,sticky=W)

Label(text="Сообщение: ".grid(row=4,column=0,sticky=W))
body_text=Text(height=10,width=45)
body_text.grid(row=4,column=1,sticky=W)

Button(text="Отправить письмо",command=send_email).grid(row=5,column=1,sticky=W)

rezult_label=Label(text="")
rezult_label.grid(row=6,column=1,sticky=W)

win.mainloop()