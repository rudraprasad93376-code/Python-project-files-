import random
import string
lenght = 10 
password = ''.join (random.choices(string.ascii_letters + string.digits, k= lenght))
print("Random password of  lenght ", lenght, ":" , password)