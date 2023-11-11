class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """     
        type str1: str
        type str2: str
        rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
           
        def gcd(a,b):
            return a if b == 0 else gcd (b,a%b)
        lenght = gcd(len(str1),len(str2))

        return str1[:lenght]
    
sol = Solution()
str1= "ABCABC"
str2= "ABC"

result = sol.gcdOfStrings(str1,str2)
print(result)
                     
        