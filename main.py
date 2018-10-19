import smtplib
from auth import *

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(auth[0], auth[1])

# Send text message through SMS gateway of destination number
server.sendmail(auth[0], auth[0], 'Do Not Nap')
