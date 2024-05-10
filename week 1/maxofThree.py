#problem link:https://www.geeksforgeeks.org/problems/greatest-of-three-numbers2520/1?page=1&category=Mathematical&difficulty=School&sortBy=submissions
class Solution:
    def greatestOfThree(self,A,B,C):
        if A>B:
            if A>C:
                return A
            return C
        else:
            if B>C:
                return B
            return C
