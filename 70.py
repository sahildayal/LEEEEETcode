'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 3:
            return n
        # return self.climbStairs(n-1) + self.climbStairs(n-2) //recursive case

        p1 = 3
        p2 = 2
        curr = 0

        for i in range(3, n):
            curr = p1+p2
            p2 = p1
            p1 = curr
        
        return curr