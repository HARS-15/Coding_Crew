#problem link:https://www.geeksforgeeks.org/problems/reverse-digit0316/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def reverse_digit(self, n):
        res=0
        while(n):
            res*=10
            res+=n%10
            n//=10
        return res
