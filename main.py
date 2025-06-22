class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        longest = ''
        for i in range(length):
            for j in range(i + 1, length + 1):
                sub = s[i:j]
                if sub == sub[::-1]:  # check if it's a palindrome
                    if len(sub) > len(longest):
                        longest = sub
        return longest

# Create an instance of the Solution class
sol = Solution()

# Define the input string
word = 'abaabacd'

# Call the method through the instance
print(sol.longestPalindrome(word))
