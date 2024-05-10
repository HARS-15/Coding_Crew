#problem link:https://www.geeksforgeeks.org/problems/sum-palindrome3857/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def isSumPalindrome (self, n):
        def reverse(n):
            ans=0
            while(n):
                ans*=10
                ans+=n%10
                n//=10
            return ans
        for i in range(6):
            k=str(n)
            if k==k[::-1]:
                return n
            n+=reverse(n)
        return -1
