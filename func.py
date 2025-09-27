# Build a module called areas inside the module need the function to calculate the volume of a sphere
# def spherearea(radius):
#     result=4/3 * 3.14 * radius*radius
#     return result
# print(spherearea(4))

# def cubiodvolume(l,w,h):
#     result=l*w*h
#     return result
# print(cubiodvolume(2,3,4))

# import math
# def euclidean_distance(x1, y1, x2, y2):
#     return math.sqrt((x2-x1)**2+(y2-y1)**2)
# x1,y1=2,5
# x2,y2=4,6
# print('Euclidean distance is:',euclidean_distance(x1,y1,x2,y2))

import math
def manhatton_distance(x1,y1,x2,y2):
    return abs((x2-x1)**2+(y2-y1)**2)
x1,y1=6,7
x2,y2=4,5
print("manhatton distance is :",manhatton_distance(x1,y1,x2,y2))
