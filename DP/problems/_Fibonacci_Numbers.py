# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from functools import lru_cache
import inspect


class Fibonacci_Numbers():

    def explanation(self):
        print(f"\nThe question provides an integer n and asks to return the n-th number in the Fibonacci sequence, with f(0) = 0, f(1) = 1")
        print(f"\nThe recurrence relation: f(i) = f(i-2) + f(i-1), which means an only choice to add f(i-2) and f(i-1) for f(i), where f(i) is the i-th # in the Fibonacci sequence, with f(0) = 0, f(1) = 1\n\nSource codes:\n")
        print(inspect.getsource(self.top_down) + '\n')
        print(inspect.getsource(self.bottom_up))

    def top_down(self, n):
        """
        Recursion + Memoization;
        Time Complexity O(n), Space Complexity O(n) for the recursion call stack
        """
        @lru_cache(maxsize=None)
        def Fibonacci(i):
            if i < 2:
                return f[i]
            return Fibonacci(i-2) + Fibonacci(i-1)
        f = [0, 1]
        return Fibonacci(n)

    def bottom_up(self, n):
        """
        Tabulation - full tabulation has Space Complexity O(n); keeping only needed items has Space Complexity O(1)
        Time Complexity O(n), Space Complexity O(1)
        """
        f = [0, 1]
        if n < 2:
            return F[n]
        for i in range(2, n+1):
            f_i = sum(f) # implementation of the recurrence relation: Fn = Fn-2 + Fn-1
            f[:] = f[1:] + [f_i] # shift to prepare for the next iteration
        return f_i

