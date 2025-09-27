# write a function that takes password as input and it is valid password using the following rules

# 1.it has to be minimun 8 chracters
# 2.the password should be mix of alphabtes and numbers
# 3.it should contain atleast one special character
# 4.it should not have spces
# 5.it should contain mix of uppercase and lowercase (optinal)

# password=input("Enter the password:")
# if len(password) < 8:
#     print("password must contain min of 8 characters")
# elif password.isalpha():
#     print("password must contain alphabtes")
# elif password.isdigit():
#     print("password must contains numeric vvalues")
# elif password.count("@")==0 and password.count("#")==0 and password.count("$")==0:
#     print("password must contin special charcters")
# elif password.count(" ")>0:
#     print("password must not have spacess")
# else:
#     print("password is invalid")                       

# create 2 lists and take input from user list1 should be even and list2 should be odd print the 2 lists even numbers should goto even list and odd numbers should go to odd list

# even_list=[]
# odd_list=[]
# num=int(input("Enter the number:"))
# if num %2 == 0:
#        even_list.append(num)
# else:
#  odd_list.append(num) 
# print("even numbers:",even_list)
# print("odd numbers:",odd_list) 

    
 

# check if an element exists in list

# list_=[1,2,3,4,5]
# if 6 in list_:
#     print("exists")
# else:
#     print("not exists") 
# print(list_)   

# cities=["Newjersy","newyork","bangkok","vience","paris","australia","london","washington d.c","delhi"]
# input_user = input("newyork","london")
# if cities.count(input_user) > 0:
#  print("exists") 
# else:
#    print("not exists") 

# my_list=["Hema","sow","ramya","puji","jeo"]
# item=input("Enter the item to check:")
# if item in my_list:
#     print("exists")
# else:
#     print("not exists")    


# cities=["veinece","newyork","newjersy","washington D.c","london","paris","Dubai","tokya"]
# # cities.extend(["sydney","delhi"])
# cities.append("newjersy")
# print(cities)

def fib(n):
    a=0
    b=1
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(7)        