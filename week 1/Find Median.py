#Problem link:https://www.geeksforgeeks.org/problems/find-the-median0527/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def find_median(self, v):
        v.sort()
        n=len(v)
        if n%2==0:
            return (v[n//2-1]+v[n//2])//2
        else:
            return v[n//2]
		
