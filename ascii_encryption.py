#This is a crypto code.
#It is shifting a character 2 ascii value.and decryption with shifting back 2 ascii value.

result = ''
message = ''
choice = ''

while choice != 0:
	choice = input("\n Do you want to encrypt or decrypt the message ? \nEnter 1 for encrypt, 2 for decrypt")


	if choice == '1':
		message = input("\n Enter message for encryption")
		for i in range(0,len(message)):
			result = result + chr(ord(message[i]) - 2)
		print(result + '\n\n')
		result = ''

	elif choice == '2' :
		message = input("\n enter message for decryption")
		for i in range(0,len(message)):
			result = result + chr(ord(message[i]) + 2)
		print(result + '\n\n')
		result = ''
