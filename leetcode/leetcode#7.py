class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output= []
        for number in range(len(nums)):
            k = 0
            answer = 1
            for multiply in nums:
                if number != k:
                    answer *= multiply
                k +=1

            output.append(answer)       

        return output
sol = Solution()
nums = [1,2,3,4]
result = sol.productExceptSelf(nums)
print(result)


