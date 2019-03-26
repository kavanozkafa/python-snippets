Unicode_string = u'\u0627\u0644\u0639\u062a\u0629'
print(Unicode_string)
encoded_string = Unicode_string.encode('unicode-escape')
print(encoded_string)
decoded_string = encoded_string.decode('unicode-escape')
print(decoded_string)

