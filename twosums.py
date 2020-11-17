class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(0, len(nums)):
            hashmap[nums[i]] = i
            compliment = target - nums[i]
            if compliment in hashmap.keys() and hashmap[compliment] != i:
                return [i, hashmap[compliment]]

sol = Solution()
print(sol.twoSum([3,3],6))