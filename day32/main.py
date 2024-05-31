import smtplib
my_email = "anhphan42891@gmail.com"
password = "xyrx nycf zgez gclw"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="anhphan42891@gmail.com",msg="Hello eiu")
connection.close()