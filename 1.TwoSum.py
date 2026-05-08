#May 7, 2026


class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range (0,len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

        