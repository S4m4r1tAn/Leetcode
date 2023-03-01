class Solution(object):
    def isPalindrome(self, x):
        x = list(x)
        y = []
        for item in x:
            y.append(item)
        y.reverse()
        return True if x == y else False
    
x = int(input('Digite um numero: '))
x_is_palindrome = Solution()
result = x_is_palindrome.isPalindrome(str(x))
print(result)