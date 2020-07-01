def xzsort(nums):
    min,x=nums[0],0
    for i in range(len(nums)-1):
        for j in range(i,len(nums)):
            if nums[j]<min:
                min=nums[j]
                x=j
        nums[x],nums[i]=nums[i],nums[x]
        min=nums[i+1]
        x=i+1
    return nums
nums=[8,3,11,2,0,7,6,20,1,9]
print(xzsort(nums))