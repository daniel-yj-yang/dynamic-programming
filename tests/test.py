# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from DP import Fibonacci_Numbers as fib
F = fib()
F.explanation()  # this will show the code and some explanations
print(F.top_down(500))
print(F.bottom_up(500))

from DP import House_Robber as robber
r = robber()
r.explanation()
print(r.top_down(nums = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]))
print(r.bottom_up(nums = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]))
