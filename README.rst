.. -*- mode: rst -*-

|BuildTest|_ |PyPi|_ |License|_ |Downloads|_ |PythonVersion|_

.. |BuildTest| image:: https://travis-ci.com/daniel-yj-yang/DynamicProgramming.svg?branch=main
.. _BuildTest: https://app.travis-ci.com/github/daniel-yj-yang/DynamicProgramming

.. |PythonVersion| image:: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue
.. _PythonVersion: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue

.. |PyPi| image:: https://img.shields.io/pypi/v/DynamicProgramming
.. _PyPi: https://pypi.python.org/pypi/DynamicProgramming

.. |Downloads| image:: https://pepy.tech/badge/DynamicProgramming
.. _Downloads: https://pepy.tech/project/DynamicProgramming

.. |License| image:: https://img.shields.io/pypi/l/DynamicProgramming
.. _License: https://pypi.python.org/pypi/DynamicProgramming


========================================
Library for Studying Dynamic Programming
========================================

DP is suitable for a particular kind of problem (computation) structure: the subproblems are highly overlapping (usually with exponential time complexity, like 2^n) and the recurrence relation can be clearly defined.

In this library, I provide implementations of two major DP approaches -- (1) top-down (recursion + memoization); (2) bottom-up (tabulation) -- for some well-known DP problems, including:

- Fibonacci_Numbers
- House_Robber
- Min_Cost_Climbing_Stairs
- Maximum_Subarray
- Best_Time_to_Buy_and_Sell_Stock
- Coin_Change
- Word_Break
- Decode_Ways


Installation
------------

.. code-block::

   pip install dynamic-programming


Sample Usage
------------

>>> from DP import Fibonacci_Numbers as fib
>>> F = fib()
>>> F.explanation() # this will show the code and some explanations 
>>> F.top_down(n = 10)
55
>>> F.bottom_up(n = 10)
55

>>> from DP import House_Robber as robber
>>> r = robber()
>>> r.explanation() # this will show the code and some explanations 
>>> r.top_down(nums = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98])
120
>>> r.bottom_up(nums = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98])
120

>>> from DP import Min_Cost_Climbing_Stairs as climb
>>> c = climb()
>>> c.explanation() # this will show the code and some explanations 
>>> c.top_down(cost = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98])
57
>>> c.bottom_up(cost = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98])
57

>>> from DP import Maximum_Subarray as maxsub
>>> m = maxsub()
>>> m.explanation() # this will show the code and some explanations 
>>> m.top_down(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4, 9, -2, 10, 15, -3, -4])
[4, -1, 2, 1, -5, 4, 9, -2, 10, 15] has the largest sum = 37.
>>> m.bottom_up(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4, 9, -2, 10, 15, -3, -4])
[4, -1, 2, 1, -5, 4, 9, -2, 10, 15] has the largest sum = 37.

>>> from DP import Best_Time_to_Buy_and_Sell_Stock as stock
>>> s = stock()
>>> s.explanation() # this will show the code and some explanations 
>>> s.top_down(prices=[7, 1, 5, 3, 6, 4, 2, 10, 2, 3, 9, 1])
9
>>> s.bottom_up(prices=[7, 1, 5, 3, 6, 4, 2, 10, 2, 3, 9, 1])
9

>>> from DP import Coin_Change as coin
>>> c = coin()
>>> c.explanation() # this will show the code and some explanations 
>>> c.top_down(coins=[1, 5, 10, 25], amount=150)
6
>>> c.bottom_up(coins=[1, 5, 10, 25], amount=150)
6

>>> from DP import Word_Break as wordbreak
>>> w = wordbreak()
>>> w.explanation() # this will show the code and some explanations 
>>> w.top_down(s = "codingisfunpythonisgreat", wordDict = ["coding", "is", "fun", "python", "great"])
True
>>> w.bottom_up(s = "codingisfunpythonisgreat", wordDict = ["coding", "is", "fun", "python", "great"])
True

>>> from DP import Decode_Ways as decode
>>> d = decode()
>>> d.explanation() # this will show the code and some explanations 
>>> d.top_down(s = "12812823")
8
>>> d.bottom_up(s = "12812823")
8
