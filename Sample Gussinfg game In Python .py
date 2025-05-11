
inputpassword = input("Enter your password: ") # user input passwprd

tries =  4 # make the numper of input spesifice and using for valdation in password

mainpassword =  "1234"  # corret to check in codiection of loop


while(mainpassword != inputpassword):
 tries-=1  # to descreen numper every wrong answer
 print(f"Wrong password {'left' if tries == 0  else tries } left chance ")
 # for short hand if
 inputpassword = input("Write your password: ")


 if (tries == 0):
   print("All Tries is Finsheed....")
   break

else:
 print("Correct password")

# num =  10
#
# print({"true" if  num> 200 else 'false' })  # for  test shor hand in f


