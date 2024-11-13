
def single(nums):
    result=0
    for i in nums:
        result=result ^ i
    return result

nums=[2,2,1,4,1]
j=print(single(nums))

#result = result ^ i performs a bitwise XOR operation between the current value of result and the current number i.
# Key Property of XOR:
# Any number XORed with itself results in 0.
# Any number XORed with 0 remains unchanged.