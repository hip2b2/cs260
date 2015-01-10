#!/usr/bin/python
# CS 260 Programming Examples
# wyu@ateneo.edu

import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.ehlo()
server.login('username','password')
server.sendmail('from email','to email','From: \r\nTo: \r\nSubject: test email\r\nTest Email Body')
server.quit()
