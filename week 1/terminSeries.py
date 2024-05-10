#problem link:https://www.geeksforgeeks.org/problems/find-n-th-term-of-series-1-3-6-10-15-215506/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def findNthTerm(self, N):
        return N*(N+1)//2
