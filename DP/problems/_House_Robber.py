# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from functools import lru_cache
import inspect


class House_Robber():

    def explanation(self):
        print(f"\nThe question provides an integer array nums for the amount of money of each house and asks you to return the max. amount of money you can rob tonight without robbing two adjacent houses.")
        print(f"\nThe recurrence relation: f(i) = max( f(i-2) + nums[i], f(i-1) ), which means a choice between (robbing house[i] and assuming all the max gain at house[i-2]) vs. (not robbing house[i] and assuming all the max. gain at house[i-1]), where f(i) is the max. gain at house[i], with f(-2) = f(-1) = 0\n\nSource codes:\n")
        print(inspect.getsource(self.top_down) + '\n')
        print(inspect.getsource(self.bottom_up))

    def top_down(self, nums = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]): # demo nums array
        """
        Recursion + Memoization;
        Time Complexity O(n), Space Complexity O(n) for the recursion call stack
        """
        @lru_cache(maxsize=None)
        def maxgain(i):
            if i < 0:
                return 0
            return max( maxgain(i-2) + nums[i], maxgain(i-1) )
        return maxgain(len(nums)-1)

    def bottom_up(self, nums=[3, 10, 3, 1, 2, 4, 10, 2, 44, 98]):  # demo nums array
        """
        Tabulation - full tabulation has Space Complexity O(n); keeping only needed items has Space Complexity O(1)
        Time Complexity O(n), Space Complexity O(1)
        """
        f_i_minus_2 = f_i_minus_1 = 0
        for num in nums:
            f_i = max( f_i_minus_2 + num, f_i_minus_1 ) # implementation of the recurrence relation: f(i) = max( f(i-2) + nums[i], f(i-1) )
            f_i_minus_2, f_i_minus_1 = f_i_minus_1, f_i # shift to prepare for the next iteration
        return f_i # f_i: the max. gain at house[i], i is 0th-indexed

