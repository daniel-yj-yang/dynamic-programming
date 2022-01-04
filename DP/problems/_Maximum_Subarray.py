# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from functools import lru_cache
import inspect

class Maximum_Subarray():

    def explanation(self):
        print(f"\nThe question provides an integer array nums and asks you to find the contiguous subarray with the max. sum.")
        print(f"\nThe recurrence relation: maxsum(i) = max(nums[i], nums[i]+maxsum(i-1)), which means a choice between (a) including maxsum(i-1) vs. (b) not including it, when calculating the max. subarray sum including nums[i], where maxsum(i) is the max. subarray ending at the i-th index, with maxsum(0) = nums[0]\n\nSource codes:\n")
        print(inspect.getsource(self.top_down) + '\n')
        print(inspect.getsource(self.bottom_up))

    def top_down(self, nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4, 9, -2, 10, 15, -3, -4]):
        """
        Recursion + Memoization;
        Time Complexity O(n), Space Complexity O(n) for the recursion call stack
        """
        @lru_cache(maxsize=None)
        def maxsum(right_i):  # return a tuple = (the max. subarray sum ending at the i-th index, the left_i for that subarray)
            nonlocal global_maxsum, global_left_i, global_right_i
            if right_i == 0:
                return (nums[0], 0)
            if maxsum(right_i-1)[0] > 0:
                maxsum_i = nums[right_i] + maxsum(right_i-1)[0]
                left_i = maxsum(right_i-1)[1]
            else:
                maxsum_i = nums[right_i]
                left_i = right_i
            if global_maxsum < maxsum_i:
                global_maxsum = maxsum_i
                global_left_i, global_right_i = left_i, right_i
            return (maxsum_i, left_i)
        global_maxsum, global_left_i, global_right_i = float('-inf'), len(nums)-1, len(nums)-1
        maxsum(len(nums)-1)
        print(f"{nums[global_left_i:global_right_i+1]} has the largest sum = {global_maxsum}.")

    def bottom_up(self, nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4, 9, -2, 10, 15, -3, -4]):
        """
        Tabulation - full tabulation has Space Complexity O(n); keeping only needed items has Space Complexity O(1)
        Time Complexity O(n), Space Complexity O(1)
        """
        maxsum_i_minus_1 = nums[0]
        left_i = 0
        global_maxsum = float('-inf')
        for right_i in range(1, len(nums)):
            if maxsum_i_minus_1 > 0:
                maxsum_i = nums[right_i] + maxsum_i_minus_1
            else:
                maxsum_i = nums[right_i]
                left_i = right_i
            if global_maxsum < maxsum_i:
                global_maxsum = maxsum_i
                global_left_i, global_right_i = left_i, right_i
            maxsum_i_minus_1 = maxsum_i
        print(f"{nums[global_left_i:global_right_i+1]} has the largest sum = {global_maxsum}.")

