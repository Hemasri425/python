# def quadrantTest(x,y):
#     if x > 0 and y > 0:
#         print("point Lies in the Q-1")
#     elif x < 0 and y > 0:
#         print("point Lies in the Q-2")
#     elif x < 0 and y < 0:
#         print("point Lies in the Q-3")
#     else:
#         print("point Lies in the Q-4")  
# quadrantTest(-2,3)                  

list1=[1,2,3,5,4]
list2=[2,6,4,5,6]
for i in list1:
    for j in list2:
        if i == j:
            print(j)
