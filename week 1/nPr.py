#problem link:https://www.geeksforgeeks.org/problems/npr4253/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def nPr(self, n, r):
        res=1
        for i in range(n,n-r,-1):
            res*=i
        return res
