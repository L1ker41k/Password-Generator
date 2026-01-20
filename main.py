import random
alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()?_"
password = ''
len_password = int(input('Укажите длину вашего пароля'))
for i in range(len_password):
    password += random.choice(alphabet)
print(password)