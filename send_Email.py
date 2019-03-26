import smtplib #simple mail transport protocol library. port number :SMTP Port: 587/465

message = 'meeting at 2 am in my room'


mail = smtplib.SMTP('smtp.gmail.com', 587) #(server,prort number)

mail.ehlo()

mail.starttls()

mail.login('example@gmail.com','123456')

mail.sendmail('from_@gmail.com','to_@gmail.com',message)

mail.close()




"""

List of SMTP and POP3 Server




Default Ports
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	Non-Encrypted 	AUTH 	25 (or 587)
Secure (TLS) 	StartTLS 	587
Secure (SSL) 	SSL 	465
POP3 Server (Incoming Messages) 	Non-Encrypted 	AUTH 	110
  	Secure (SSL) 	SSL 	995
 
Gmail
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.gmail.com 	SSL 	465
  	smtp.gmail.com 	StartTLS 	587
POP3 Server (Incoming Messages) 	pop.gmail.com 	SSL 	995
  	Please make sure, that POP3 access is enabled in the account settings.
Login to your account and enable POP3.
 
Outlook.com
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.live.com 	StartTLS 	587
POP3 Server (Incoming Messages) 	pop3.live.com 	SSL 	995
 
Office365.com
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.office365.com 	StartTLS 	587
POP3 Server (Incoming Messages) 	outlook.office365.com 	SSL 	995
  	Note: If the above settings are not working for your account, then login to the outlook web app, go to the "Settings" > "Options" > "Account" > "My Account" > "Settings for POP and IMAP Access".
 
Yahoo Mail
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.mail.yahoo.com 	SSL 	465
POP3 Server (Incoming Messages) 	pop.mail.yahoo.com 	SSL 	995
 
Yahoo Mail Plus
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	plus.smtp.mail.yahoo.com 	SSL 	465
POP3 Server (Incoming Messages) 	plus.pop.mail.yahoo.com 	SSL 	995
 
Yahoo UK
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.mail.yahoo.co.uk 	SSL 	465
POP3 Server (Incoming Messages) 	pop.mail.yahoo.co.uk 	SSL 	995
 
Yahoo Deutschland
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.mail.yahoo.com 	SSL 	465
POP3 Server (Incoming Messages) 	pop.mail.yahoo.com 	SSL 	995
 
Yahoo AU/NZ
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.mail.yahoo.com.au 	SSL 	465
POP3 Server (Incoming Messages) 	pop.mail.yahoo.com.au 	SSL 	995
 
O2
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.o2.ie 	  	25
POP3 Server (Incoming Messages) 	pop3.o2.ie 	  	110
 
O2.uk
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.o2.co.uk 	  	25
POP3 Server (Incoming Messages) 	pop3.o2.co.uk 	  	110
 
AT&T
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.att.yahoo.com 	SSL 	465
POP3 Server (Incoming Messages) 	pop.att.yahoo.com 	SSL 	995
 
NTL @ntlworld.com
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.ntlworld.com 	SSL 	465
POP3 Server (Incoming Messages) 	pop.ntlworld.com 	SSL 	995
 
BT Connect
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	pop3.btconnect.com 	  	25
POP3 Server (Incoming Messages) 	mail.btconnect.com 	  	110
 
BT Openworld
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	mail.btopenworld.com 	  	25
POP3 Server (Incoming Messages) 	mail.btopenworld.com 	  	110
 
BT Internet
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	mail.btinternet.com 	  	25
POP3 Server (Incoming Messages) 	mail.btinternet.com 	  	110
 
Orange
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.orange.net 	  	25
POP3 Server (Incoming Messages) 	pop.orange.net 	  	110
 
Orange.uk
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.orange.co.uk 	  	25
POP3 Server (Incoming Messages) 	pop.orange.co.uk 	  	110
 
Wanadoo UK
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.wanadoo.co.uk 	  	25
POP3 Server (Incoming Messages) 	pop.wanadoo.co.uk 	  	110
 
Hotmail
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.live.com 	SSL 	465
POP3 Server (Incoming Messages) 	pop3.live.com 	SSL 	995
 
O2 Online Deutschland
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	mail.o2online.de 	  	25
POP3 Server (Incoming Messages) 	pop.o2online.de 	  	110
 
T-Online Deutschland
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	securesmtp.t-online.de 	StartTLS 	587
POP3 Server (Incoming Messages) 	securepop.t-online.de 	SSL 	995
 
1&1 (1and1)
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.1and1.com 	StartTLS 	587
POP3 Server (Incoming Messages) 	pop.1and1.com 	SSL 	995
 
1&1 Deutschland
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.1und1.de 	StartTLS 	587
POP3 Server (Incoming Messages) 	pop.1und1.de 	SSL 	995
 
Comcast
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.comcast.net 	  	587
POP3 Server (Incoming Messages) 	mail.comcast.net 	  	110
 
Verizon
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	outgoing.verizon.net 	SSL 	465
POP3 Server (Incoming Messages) 	incoming.verizon.net 	SSL 	995
 
Verizon (Yahoo hosted)
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	outgoing.yahoo.verizon.net 	  	587
POP3 Server (Incoming Messages) 	incoming.yahoo.verizon.net 	110
 
zoho Mail
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.zoho.com 	SSL 	465
IMAP Server (Incoming Messages) 	pop.zoho.com 	SSL 	995
 
Mail.com
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.mail.com 	SSL 	465
IMAP Server (Incoming Messages) 	pop.mail.com 	SSL 	995
 
GMX.com
	Server: 	Authentication: 	Port:
SMTP Server (Outgoing Messages) 	smtp.gmx.com 	SSL 	465
IMAP Server (Incoming Messages) 	pop.gmx.com 	SSL 	995



"""