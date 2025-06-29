'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
'''

class Solution:
    def sortArray(self, nums: List[int])-> List[int]:
        def merge(nums, start, middle, end):
            L = nums[start : middle+1]
            R = nums[middle+1 : end+1]

            i, j = 0, 0
            k = start

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i+=1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1

        def mergeSort(nums, start, end):
            if start >= end:
                return 
            
            middle = (start+end) // 2
            mergeSort(nums, start, middle)
            mergeSort(nums, middle+1, end)
            merge(nums, start, middle, end)

        mergeSort(nums, 0, len(nums)-1)
        return nums

''''
Inseertion sort but Exceeded run time
'''
        # for i in range(1, len(nums)):
        #     j = i-1
        #     while j>=0 and nums[j+1] < nums[j]:
        #         t = nums[j+1]
        #         nums[j+1] = nums[j]
        #         nums[j] = t
        #         j -= 1
        # return nums
        