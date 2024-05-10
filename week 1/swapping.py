#problem link:https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def get(self, a, b):
        a=a+b
        b=a-b
        a=a-b
        return [a,b]
