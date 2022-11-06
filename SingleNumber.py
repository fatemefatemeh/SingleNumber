def SingleNumber(nums):
    for i in nums:
        c=nums.count(i)
        if c==1:
            print(i)
            break
nums=[4,4,5,1,1,3,3]
print(SingleNumber(nums))


