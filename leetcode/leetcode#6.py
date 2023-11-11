class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])
sol = Solution()
s= "blue is sky the"
result = sol.reverseWords(s)
print(result)
"""
  def reveres():
            reverss = s.split()
            for i in range(1,len(reverss)+2):
                if i%2 == 1:
                    reverss.insert(i," ")
            return "".join(reverss)
        return reveres()
    
"""