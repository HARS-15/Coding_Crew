#problem link:https://www.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not2751/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def isDigitSumPalindrome(self, n):
        res=0
        while(n):
            res+=n%10
            n//=10
        if res<10:
            return 1
        else:
            if res%10==res//10:
                return 1
            else:
                return 0
