#problem link:https://www.geeksforgeeks.org/problems/print-table0303/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def getTable(self,N):
        l=[]
        for i in range(1,11):
            l.append(N*i)
        return l
