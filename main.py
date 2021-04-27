import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('worldomedia1@gmail.com', '9874792606')
server.sendmail('worldomedia1@gmail.com',
                'pal.suparno2001@gmail.com',
                'Hey Suparno! How are you you doing? Hope to see you soon as I am going there soon')
