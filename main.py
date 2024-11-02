import smtplib
from email.message import EmailMessage

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