
self = 0
nums = [0,2,1,5,3,4]

def buildArray(self, nums):
    result = [0] * len(nums)
    for i in range(len(nums)):
        result[i] = nums[nums[i]]
    return result

print(buildArray(self, nums))