import random

LettersNsymbols  = 'abcdefghijkmnopqrstuvwxyz123456789ABCDEFGHIJKMNOPQRSTUVWXYZ!"#$%&/()=?¡'

numbers = input('Introduce la cantidad de contraseñas que desea generar -')
numbers = int(numbers) 

LengthPassword =input('¿De cuantos caracteres desea que sea su contraseña? - ')
LengthPassword =int(LengthPassword)

for contraseñaNumerica in range(numbers):
    password = ''
    for contraseñaLongitudad in range(LengthPassword):
        password += random.choice(LettersNsymbols)
    print(password)  
