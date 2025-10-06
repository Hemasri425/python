def motion_type(position):
    gap=position[1]-position[0]
    for i in range(len(position)-1):
        if position[i+1]-position[i]!=gap:
            return "Non-uniform motion"
    return "uniform motion"
print(motion_type([0,10,20,30,40]))
    