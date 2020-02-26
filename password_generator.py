# generating a password in the range 5-10 characters with atleast 1 lowers case 1 uppercase 1 number and 1 symbols

from random import * 
import string
import random
def pwgen(size=randint(5,10)):
    if size<=4:
        print( "size should be above 4 character")
    elif size>10:
        print("size should be less than or equal to 10 charcters")    
    else:

        a=string.ascii_letters+string.digits+string.punctuation
        b=''.join(random.sample(a,size-4))
        c=random.choice(string.ascii_uppercase)+b+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
        return (c)
      
password=pwgen()           
print(password)