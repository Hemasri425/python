def calculate_roi(initial_price,final_price):
    roi_list=[]
    for i in range(len(initial_price)):
        roi=((final_price[i]-initial_price[i])/initial_price[i])*100
        roi_list.append(roi)
    return roi_list
Intial=[100,200,150]
final=[120,250,180]
print(calculate_roi(Intial,final))    