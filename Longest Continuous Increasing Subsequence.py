
def findLengthOfLCIS(nums):
    if not nums:
        return 0
    max_len=1
    current_len=1
    for i in range(1,len(nums)):
        if(nums[i]>nums[i-1]):
            current_len+=1
            max_len=max(current_len,max_len)
        else:
            current_len=1
    return max_len
nums = [1,3,5,4,7]
print(findLengthOfLCIS(nums)) #3
