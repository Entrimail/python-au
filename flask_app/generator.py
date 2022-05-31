import random


def generate_password():
    n = random.randint(8, 16) 
    psw = ''
    for i in range (n):            
        psw += random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    return f'{psw}'
