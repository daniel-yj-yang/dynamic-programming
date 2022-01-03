# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from functools import lru_cache
import inspect


class Fibonacci_numbers():

    def explanation(self):
        print(f"\nThe recurrence relation: Fn = Fn-2 + Fn-1, with F0 = 0, F1 = 1\n\nSource codes:\n")
        print(inspect.getsource(self.top_down) + '\n')
        print(inspect.getsource(self.bottom_up))

    @lru_cache(maxsize=None)
    def top_down(self, n):
        """
        Recursion + Memoization;
        Time Complexity O(n), Space Complexity O(n) for the recursion call stack
        """
        F = [0, 1]
        if n < 2:
            return F[n]
        return self.top_down(n-2) + self.top_down(n-1)

    def bottom_up(self, n):
        """
        Tabulation - full tabulation has Space Complexity O(n); keeping only needed items has Space Complexity O(1)
        Time Complexity O(n), Space Complexity O(1)
        """
        F = [0, 1]
        if n < 2:
            return F[n]
        for i in range(2, n+1):
            F_i = sum(F) # implementation of the recurrence relation: Fn = Fn-2 + Fn-1
            F[:] = F[1:] + [F_i] # shift to prepare for the next iteration
        return F_i

