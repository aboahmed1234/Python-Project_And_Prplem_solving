def translation(str):  # take a string and make loop in str
    translateor ="" # varibel to store the new str after proccess
    for letter in str: #make loop in text throw each char in str
        if letter.lower() in "eaiou": # make condation to check
            #if there any letter of thes list by membership operoter
            if letter.isupper(): #  ask if is it leeter input is upper
                translateor = translateor + "Z" #make Thes process
            else:
                translateor =  translateor + "z" # means the leeter in list
            # but it is lower
        else:  # the letter not in list  stay in it
            translateor =  translateor +  letter
    return translateor
print(translation(input("enter a text")))