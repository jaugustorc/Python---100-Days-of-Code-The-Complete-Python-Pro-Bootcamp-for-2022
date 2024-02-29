import smtplib
     
server = "smtp.gmail.com"
     
connection = smtplib.SMTP(server, 587)
connection.set_debuglevel(1)
connection.starttls()

connection.close()