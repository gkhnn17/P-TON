class Solution(object):
    def reverseVowels(self,s):
        """
        :type s: str
        :rtype: str
        """ 
        vowels=[]
        vowelsindx=[]
        k= 0
        for i in s:
            if i in 'aeiouAEIOU':
                vowels.append(i)
                vowelsindx.append(k)
            k +=1

        def getreverse():
            vowels.reverse()
            lists = list(s)
            r = 0 
            for i in vowelsindx:
                lists[i] = vowels[r]
                r +=1
            return "".join(lists)

        return getreverse()
    
sol = Solution()
str = "hello"
result =sol.reverseVowels(str)
print(result)
        
"""
class Solution(object):
    def reverseVowels(self, s):
        vowels = [char for char in s if char.lower() in 'aeiou']
        return ''.join(
            char if char.lower() not in 'aeiou' else vowels.pop()
            for char in s
        )
"""
            

