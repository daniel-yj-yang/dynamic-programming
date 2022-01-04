# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from DP import Fibonacci_Numbers as fib
F = fib()
F.explanation()  # this will show the code and some explanations
print(F.top_down(n = 500))
print(F.bottom_up(n = 500))


from DP import House_Robber as robber
r = robber()
r.explanation()
print(r.top_down(nums = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]))
print(r.bottom_up(nums = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]))


from DP import Min_Cost_Climbing_Stairs as climb
c = climb()
c.explanation() # this will show the code and some explanations 
print(c.top_down(cost = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]))
print(c.bottom_up(cost = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]))


from DP import Maximum_Subarray as maxsub
m = maxsub()
m.explanation() # this will show the code and some explanations 
print(m.top_down(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4, 9, -2, 10, 15, -3, -4]))
print(m.bottom_up(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4, 9, -2, 10, 15, -3, -4]))
