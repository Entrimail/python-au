import random
from tkinter import N


def generate_password():
    N = random.randint(8, 16) 
  
    psw = ''
    for i in range (N):
            
        psw = psw + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    return f'{psw}'
