#problem link:https://www.geeksforgeeks.org/problems/average4856/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def streamAvg(self, arr, n):
        s=0
        res=[]
        for i in range(len(arr)):
            s+=arr[i]
            res.append(s/(i+1))
        return res

