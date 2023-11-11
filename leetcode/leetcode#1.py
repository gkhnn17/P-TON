class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ""
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            merged += word1[i] + word2[j]
            i += 1
            j += 1

        # Append remaining characters from word1, if any
        merged += word1[i:]

        # Append remaining characters from word2, if any
        merged += word2[j:]

        return merged
    
# Create an instance of the Solution class
sol = Solution()

# Call the mergeAlternately method on the instance
word1 = "abc"
word2 = "defgh"
result = sol.mergeAlternately(word1, word2)

# Print the merged string
print(result)