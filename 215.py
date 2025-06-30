'''
Kth largest element in array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k

        def quick_sort(left, right):
            pivot = nums[right]
            low = left
            high = right

            while low <= high:
                while low<=high and nums[low]<pivot:
                    low += 1
                while low<=high and nums[high]>pivot:
                    high -= 1
                if low<=high:
                    nums[low], nums[high] = nums[high], nums[low]
                    low += 1
                    high -= 1

            if k<=high:
                return quick_sort(left, high)
            elif k >= low:
                return quick_sort(low, right)
            else:
                return nums[k]
            
        return quick_sort(0, len(nums)-1)
    