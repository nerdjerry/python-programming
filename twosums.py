class Solution:
    def twoSum(self, nums, target):
        numsInverse = []
        for a in nums:
            numsInverse.append(target-a)
        numsSet = set(nums)
        numsInverseSet = set(numsInverse)
        intersectSet = numsSet.intersection(numsInverseSet)
        return list(intersectSet)

sol = Solution()
print(sol.twoSum([2,7,11,15],9))