import random
import string
print(string.printable)
char_seq = ("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()+,-?:;<=>?@[/]^_'{|}~")
print(type(char_seq))
print("Enter the required length of the password rangin from 8 to 16:")
length = int(input())

if length >= 8 and length <= 16:
    password =""
    for len in range(length):
        random_char = random.choice(char_seq)
        password += random_char
           #print(password)
    list_pass = list(password)
    random.shuffle(list_pass)
    final_password ="".join(list_pass)
    print(final_password)
else:
    print("Enter a suitable range")
    
        
    
