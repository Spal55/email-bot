import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('my email id', 'my password')
server.sendmail('my email id',
                'email id of reciever',
                'Hey Suparno! How are you you doing? Hope to see you soon as I am going there soon')
