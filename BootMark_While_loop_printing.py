
mylistweb =[]


maxelements =5


while (maxelements > 0): #list is empty

    web =  input("Enter the web address : ")

    mylistweb.append(f"https:// {web.strip().lower()}")

    maxelements-=1

    print(f"website added successfully {maxelements} left ")

    print(mylistweb)

else:
 print("BootMark Is full loop is Done can not add more ")


# check if list is full print list sorted
if ( len(mylistweb) > 0 ): # list full make sort
    mylistweb.sort()
    print("printing The List in BootMark ")

    index = 0

    while (index < len(mylistweb)):
        print( mylistweb[index])
        index+=1



