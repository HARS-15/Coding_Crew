#problem Link:https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def armstrongNumber (self, n):
        res=n
        ans=0
        while(n):
            ans+=(n%10)**3
            n=n//10
        if res==ans:
            return "Yes"
        else:
            return "No"
