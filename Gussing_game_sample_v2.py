correct_password = "12345"  # true pass for validation
code = ""  # code for input user
start_count = 0  # for making condation aboyt start and end of nums of input
end_count = 4  # for end the the condation about nums of tries of input password

out_of_gussing = False  # boolen value for making the condation for password and nums of tries

while (code != correct_password and not out_of_gussing):
    # make input code untile pass != inputpass and bool val for nums input is flase
    if start_count < end_count:  # for evry nums of try until end cound
        start_count += 1  # first from start and to end
        code = input("Enter code: ")
    else:
        out_of_gussing = True  # limit of tries true must == nums of limit

if out_of_gussing: #out of range and gyssing true 
    print("you Lose Good luck")
else:
    print("Congrationsilition you Win")








