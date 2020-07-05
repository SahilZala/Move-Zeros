class Solution(object):
    def moveZeroes(self, nums):
        zeros = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == 0:
                    zeros.append(nums[j])
                    nums.pop(j)
                    break
        for i in zeros:
            nums.append(i)
        return nums


s = Solution()
print(s.moveZeroes([0,1,0,3,12]))