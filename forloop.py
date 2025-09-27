
# n=int(input("enter the number"))
# sum=0
# for i in range(n):
#         sum=sum + i        
# print(sum)        

# L1=[1,2,5,7,10]
# L2=[8,12,9,20,50]
# add_list=[]
# for i in range(5):
#     result=L1[i]+L2[i]
#     add_list.append(result)
# print(add_list)    


# n="mississippi"
# num=list(n)
# count_dict={}
# for i in num:
#     count_dict[i]=num.count(i)
# print(count_dict)    
    
# n=["Dog","F","Horn","Flight"]
# dict_list={}
# for i in ["Dog","F","Horn","Flight"]:
#     dict_list[i]=len(i)
# print(dict_list)    


# odd_list=[]
# for i in range(1,100):
#     if i%2!=0:
#         odd_list.append(i)
# print(odd_list)        

dict_={}
for i in range(1,101):
    if i%2==0:
        dict_[i]=i**2
print(dict_)        