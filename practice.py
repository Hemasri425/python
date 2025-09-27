# n=0
# odd_list=[]
# while n<100:
#     if n%2 !=0:
#         odd_list.append(n)
#     n=n+1
# print(odd_list)        


# n=0
# dict_={}
# while n <100:
#     if n%2 == 0:
#         dict_[n]=n**2
#     n=n+1
# print(dict_) 

# n=1
# while n <= 10:
#     print("4x",n,"=",4*n)
#     n=n+1       


# list_=['A','B','C','D','E','F','G','H']
# n=0
# odd_list=[]
# even_list=[]
# while n < 8:
#     if n%2==0:
#         even_list.append(n)
#     else:
#         odd_list.append(n)
#     n=n+1
# print(even_list,odd_list)            


# n=int(input("enter the number:"))
# sum=0
# for i in range(n):
#     sum=sum+i
# print(sum)    


# L1=[1,2,5,7,10]
# L2=[8,12,9,20,50]
# add_list=[]
# for i in range(5):
#     result=L1[i]+L2[i]
#     add_list.append(result)
# print(add_list)    


# n="Mississippi"
# num=list(n)
# dict_={}
# for i in num:
#     dict_[i]=num.count(i)
# print(dict_)    

# # 

# user_loc=(1,2)
# D1=(2,3)
# D2=(8,11)
# def distance(p1,p2):
#     return((p2[0]-p1[0]**2)+(p2[1]-p2[0]**2))**0.5
# d1=distance(user_loc,D1)
# d2=distance(user_loc,D2)
# if d1<d2:
#     print("allocate d1")
# else:
#     print("alloacte d2")    


# print([i for i in range(1,21)])

# n=[]
# i=0
# while i <=50:
#     if i%2==0:
#         n.append(i)
#     i=i+1
# print(n)        

# print([i**2 for i in range(1,11)])

# list=[2,5,7,10,3]
# sum=0
# for i in list:
#     sum=sum+i
# print(sum)    


# n=[1,4,5,6,9,12]
# even_list=[]
# for num in n:
#      if  num%2 == 0:
#          even_list.append(num)
# print(even_list)

# for i in range(1,11):
#     print("5 x",i,"=",5 * i)

# n=[10,20,30]
# print(max(n))
 
# n="Hemasri"
# print(n[::-1])

# sum=0
# for i in range(1,101):
#     sum=sum+i
# print(sum)    

# num=1234
# rev=0
# while num > 0:
#     digit = num % 10
#     rev = rev*10+digit
#     num=num//10
# print(rev)    

# num=123456
# rev=0
# while num > 0:
#     digit= num % 10
#     rev=rev*10+digit
#     num=num//10
# print(rev)    

# num=0
# for i in range(1,50):
#     if i % 2 ==0:
#         print(i)

# num=12345678
# for i in str(num):
#     print(len(str(num)))

# def fib(n):
#     a=0
#     b=1
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(a+b)
# fib(7)             
            

# print([num, for num in range(1,51),if num %2==0])


# class car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#     def show(self):
#         print(self.brand)
#         print(self.color)
# car1=car("kia","white")
# car1.show()
        

            
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def getname(self):
#         self.name=name 
#     def getmarks(self):
#         self.marks=marks
#     def __str__(self):
#         return f" {self.name},{self.marks}"    
# student1=student("Hemasri",98)
# student2=student("Ramyasri",89)
# print(student1)
# print(student2)        

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def getlength(self):
#         self.length=length
#     def getbreadth(self):
#         self.breadth=breadth
#     def areaRect(self):
#         return self.length*self.breadth
#     def __str__(self):
#          return f" {self.areaRect()}"
# Rectangle_1=Rectangle(2,3)
# print(Rectangle_1)                

# class BankAccount:
#     def __init__(self,balance=0):
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance-=amount        


# even_list=[]
# L1=[1,2,5,7,10]
# L2=[8,12,9,20,50]
# for i in range(5):
#     result=L1[i]+L2[i]
#     even_list.append(result)
# print(even_list)    

# n="mississippi"
# num=list(n)
# dict={}
# for i in num:
#     dict[i]=num.count(i)
# print(dict)    


input=["dog","f","horn","fight"]
dict={}
for i in input:
    dict[i]=len(i)
print(dict)    