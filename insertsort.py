def insertSort(list):
    for i in range(1,len(list)):
        j = i-1
        key = list[i]
        while j >= 0:
            if list[j] > key:
                list[j+1] = list[j]
                list[j] = key
            j -= 1
    return list
list=[5,6,3,4,9,7,2,1,8]
print(insertSort(list))