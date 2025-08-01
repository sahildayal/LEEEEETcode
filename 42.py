'''
42. Trapping rain water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_water = 0
        left_max = height[l]
        right_max = height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                if left_max > height[l]:
                    max_water += left_max - height[l]
            else: #right_max > left_max
                r -= 1
                if right_max > height[r]:
                    max_water += right_max - height[r]

            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

        return max_water