inputpassword =  input("enter Your password:  ").strip() # user input password

correct_password = "12345"  # for Validation of password and tesing about input password

numsoftries = 4  # to force user to input a spicefic nums of try

while(inputpassword != correct_password):
    print("Wrond pasword....") # Wrongpassword try again
    numsoftries-=1 #calc The First num Of Try

    inputpassword = input(f"enter Your password again: {numsoftries} chance left ").strip()  # user input password

    if (numsoftries == 1 and inputpassword != correct_password): # emptyy nums of  tries
        print("All input password is wrong bye bye")
        break
    # else:
    #     print("correct password")

else:
    print("Correct password....")

