#problem link:https://www.geeksforgeeks.org/problems/number-of-divisors1631/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def count_divisors(self, N):
        c=0
        k=N**0.5
        for i in range(1,int(k)+1):
            if N%i==0:
                if i%3==0:
                    c+=1
                if (N//i)%3==0:
                    c+=1
        if int(k)==k and k%3==0:
            c-=1
        return c
