import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587)
print(conn.ehlo())
print(conn.starttls())
conn.login('tejas.chougule1994@gmail.com','7040360191')
conn.sendmail('tejas.chougule1994@gmail.com', 'tejas.chougule1994@gmail.com', 'Subject: Application for Developer. \n\n Dear Sir/Madam, \n I am Tejas Chougule got to know the job posting of your in python developer. \n Here by attaching my CV kindly have a look and feel free to contact me.\n\n Regards, \n\n Tejas')
conn.quit()