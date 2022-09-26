alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
crypting_message = input("Введите зашифрованное сообщение на английском ")
key = int(input("Введите длину ключа от 1 до 25 "))
crypting_message = crypting_message.lower()
crypt_message = ""
for letter in crypting_message:
	position = alphabet.find(letter)
	new_position = position + key
	if letter in alphabet:
		crypt_message += alphabet[new_position]
	else:
		crypt_message += letter
print("Ваше зашифрованное сообщение", crypt_message)
decrypt = input("Хотите расшифровать сообщение? Да/Нет")
if decrypt == "Да":
	print(crypting_message)
if decrypt == "Нет":
	print("Сообщение зашифровано")