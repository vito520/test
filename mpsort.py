def mpsort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums
nums=[5,2,6,3,9,4,11,2,5,1]
print(mpsort(nums))