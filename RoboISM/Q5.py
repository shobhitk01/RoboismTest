def dupfinder(list1):
    list1.sort
    i=0
    while i < len(list1):
        if list[i]==list[i+1]:
            return list[i]
        i=i+1

print(dupfinder([1,2,3,4,8,6,5,8,9]))