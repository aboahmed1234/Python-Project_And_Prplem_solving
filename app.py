
admins  = ["Ahmed" ,"Ali" ,"Samah" ,"Gamer"]


# print(admins)
# admins[admins.index("Samah")] = "Playstation5"
# print(admins)
name = input("Enter your name: ").strip().capitalize()
if (name in admins):
    print(f" Hello Welcome {name} back")
    options = input("Delete OR Update Your name ").strip().capitalize()
    if (options == "Update"  or options =="U"):
        thenewname = input("Enter your new name ").strip().capitalize()
        admins[admins.index(name)] = thenewname
        print("name updated successfully")
        print(admins)

    elif (options == "Delete" or options == "D"):
        admins.remove(name)
        print("name deleted successfully")
        print(admins)
    else:
        print("Invalid option")
else:
    print("You Are Not admin ")

status =  input("Not admin enter status (Y | N) ").strip().capitalize()
if ( status == "Yes" or status == "Y"):
     print("You Have Been Added")
     admins.append(name)
     print(admins)

else:
  print("You Are Not admin")
 
 
 