import smtplib
from auth import auth, destination
from email.mime.text import MIMEText as text

m = text("Please Don't")
m["Subject"] = "Don't Nap Dude"

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(auth["Login"], auth["Password"])

server.sendmail(auth["Login"], destination, m.as_string())
