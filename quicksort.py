def quickSort(list,start,end):#start,end 是指指针
    i,j = start,end
    if start<end:
        base =list[i] #设置基准数为i,即为start
        while i<j:
            while(i<j) and list[j]>=base: #找到比基准数小的数字
                j-=1#将炮兵j向左移动
            list[i] = list [j] #将找到的j复制给i
        # 同样的方法执行前半区域   
            while(i<j) and list[i]<=base:
                i+=1
            list[j]=list[i]
        list[i]=base #i=j,即将这个数设置为base
    
        quickSort(list,start,i-1)
        quickSort(list,j+1,end)
    return list

print(quickSort([4,5,9,1,8,2,7,3],0,7))