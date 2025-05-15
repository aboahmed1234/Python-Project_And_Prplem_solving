# create a Script for generate a password with Upeercase and lower case
# and puncationtion

# 1-import modules for use

import  string  # for funcation upper case and lowercase
import random #making shuffle

# 2- create vribles to store in it the requrments of password and convert it into list
# like(upper case - lowe case digtes and piuncationction from module string)

s1 =  list(string.ascii_uppercase)
s2 =  list(string.ascii_lowercase)
s3= list(string.digits)
s4=  list(string.punctuation)

# 3 - take input nums of character from user and make valadion
# input must be int and at least 6 digts

charcter_password = input("How Many Nums Of Charcters: ")

while True:
    try:
        charcter_password = int(charcter_password) # for make sure that num is int
        if charcter_password < 6:
            print("Enter At least 6 Charcters: ")
            charcter_password =  input("enter The Numper again: ")
        else:
            break

    except:
        print("enter nums only: ")
        charcter_password =  input("How Many Nums Of Charcters: ")

# 4- shuufles Thes nums by random module


random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


# 5-cals The 30% of charcter and sroe it in varibel
# and 20% for 20 For nums and calc using round for 30% and 20%


part1 = round(charcter_password * (30/100))
part2 = round(charcter_password * (20/100))


# 6 carete passsword as empty list and make loop for
# every part in all part and append it
#  make join for theses part and prant password after join


password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])


for i in range(part2):
    password.append(s3[i])
    password.append((s4[i]))


password = "".join(password[0:])

print(password)














