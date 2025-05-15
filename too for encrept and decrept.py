# make a tool for encreption and decription
#  import modules

# --------------------------------------
# 1- import string and random modukes
import string
import random
from operator import index

# Declere vrible to store all encrept text

all_char = string.ascii_letters + string.digits + string.punctuation + " "


# - convert a string to list

all_char = list(all_char)

# 3- make copy of this list to store key for encreption and decreption


key =  all_char.copy()


# make shuffle for key to generete random text

random.shuffle(key)

print("--------------------Encrepetion---------------------------")

#  take a plain text and make loop in it and find index of everu ykey
# for encrepption

plain_text = input("enter a text for encrept:  ")
cipher_text = ""

for letter in plain_text:
    index = all_char.index(letter)
    cipher_text+=key[index]

print(f"Encrept is.........  {cipher_text}")


print("--------------------------Decrept--------------------------")

cipher_text = input("enter a text to decrept:  ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text+=all_char[index]

print(f"Decrept.............  {plain_text}")















