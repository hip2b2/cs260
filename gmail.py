#!/usr/bin/python
# CS 260 Programming Examples
# wyu@ateneo.edu

import smtplib

# connect to publicly accessible SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)

# in this case, this SMTP only accepts TLS encrypted sessions
server.starttls()

# check and display capabilities of server
print server.ehlo()

# login to server, this SMTP only accepts logged in sessions
server.login('temp@gmail.com','temp')

# send an email
server.sendmail('temp@gmail.com','wyu@ateneo.edu','From: \r\nTo: \r\nSubject: test email\r\nTest Email Body')

# exit when done
server.quit()
