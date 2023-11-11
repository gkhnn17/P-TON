class Solution(object):
    def canPlaceFlowers(self,flowerbed,n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0,0)
        flowerbed.append(0)
        canplace=[]
        for i in range (1,len(flowerbed)-1):
            zeroindex = flowerbed[i]
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0  :
                flowerbed[i] = 1
                canplace.append(1)

        if sum(canplace)>=n:
            return True,flowerbed
        
        return False,flowerbed
            

     
sol=Solution()
flowerbed=[1,0,0,0,1]
n = 2
result=sol.canPlaceFlowers(flowerbed,n)
print(result)