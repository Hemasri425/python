def minmax(data):
    smallest=data[0]
    largest=data[0]
    for num in data:
        if num < smallest:
            smallest=num
        if num > largest:
            largest=num
    return smallest,largest
print(minmax([4,7,1,9,3]))            