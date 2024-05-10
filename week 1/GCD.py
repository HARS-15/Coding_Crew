#Problem link:https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def gcd(self, a : int, b : int) -> int:
        while(b):
            a,b=b,a%b
        return a
