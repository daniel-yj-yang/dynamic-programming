# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from DP import Fibonacci_Numbers as fib
F = fib()
F.explanation()  # this will show the code and some explanations
print(F.top_down(n = 500))
print(F.bottom_up(n = 500))

print('\n---------------------------------------------------------------------------------------------------')

from DP import House_Robber as robber
r = robber()
r.explanation()
print(r.top_down(nums = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]))
print(r.bottom_up(nums = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]))

print('\n---------------------------------------------------------------------------------------------------')

from DP import Min_Cost_Climbing_Stairs as climb
c = climb()
c.explanation() # this will show the code and some explanations 
print(c.top_down(cost = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]))
print(c.bottom_up(cost = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]))

print('\n---------------------------------------------------------------------------------------------------')

from DP import Maximum_Subarray as maxsub
m = maxsub()
m.explanation() # this will show the code and some explanations 
print(m.top_down(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4, 9, -2, 10, 15, -3, -4]))
print(m.bottom_up(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4, 9, -2, 10, 15, -3, -4]))

print('\n---------------------------------------------------------------------------------------------------')

from DP import Best_Time_to_Buy_and_Sell_Stock as stock
s = stock()
s.explanation()  # this will show the code and some explanations
print(s.top_down(prices=[7, 1, 5, 3, 6, 4, 2, 10, 2, 3, 9, 1]))
print(s.bottom_up(prices=[7, 1, 5, 3, 6, 4, 2, 10, 2, 3, 9, 1]))

print('\n---------------------------------------------------------------------------------------------------')

from DP import Coin_Change as coin
c = coin()
c.explanation()  # this will show the code and some explanations
print(c.top_down(coins=[1, 5, 10, 25], amount=150))
print(c.bottom_up(coins=[1, 5, 10, 25], amount=150))

print('\n---------------------------------------------------------------------------------------------------')

from DP import Word_Break as wbreak
w = wbreak()
w.explanation()  # this will show the code and some explanations
print(w.top_down(s="codingisfunpythonisgreat", wordDict=["coding", "is", "fun", "python", "great"]))
print(w.bottom_up(s="codingisfunpythonisgreat", wordDict=["coding", "is", "fun", "python", "great"]))

print('\n---------------------------------------------------------------------------------------------------')

from DP import Decode_Ways as decode
d = decode()
d.explanation()  # this will show the code and some explanations
print(d.top_down(s="12812823"))
print(d.bottom_up(s="12812823"))
