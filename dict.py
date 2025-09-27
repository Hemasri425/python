# Take a username and password from user and store it in dictionary 
# store 3 usernames and paawords
#when the user enters the username if the username does not exists in the dict, ask the user to signup.. else print the message user exists

dict_={"Hema.kommalapati@gmail.com":["Hemasri",22,"Hema@12"],"sowjii123@gmail.com":["sowjanya",21,"sow@34"],"Ramyagunturu_23@gmail.com":["Ramyasri",23,"Ramya$12"]}
user_=input("Enter the username:")
if dict_.get(user_) == None:
    print("signup for newaccount")
else:
    print("exists")    





