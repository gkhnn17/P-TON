class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        list = []
        for i in range (len(candies)):
            maxi = candies[i]+ extraCandies
            list.append(maxi >= max(candies))

        return list
    
sol = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
result = sol.kidsWithCandies(candies,extraCandies)
print(result)
            
                    
            
