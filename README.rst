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

DP is suitable for a particular kind of problem structure: the subproblems are highly overlapping (usually with 2^n time complexity) and the recurrence relation can be clearly defined.

In this library, I try to provide implementations of two major DP approaches -- (1) top-down (recursion + memoization); (2) bottom-up (tabulation) -- for some well-known DP problems.


Installation
------------

.. code-block::

   pip install DynamicProgramming


Sample Usage
------------

>>> from DP import Fibonacci_numbers as fib
>>> F = fib()
>>> F.explanation()

The recurrence relation: Fn = Fn-2 + Fn-1, with F0 = 0, F1 = 1

Source codes:

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
        Tabulation;
        Time Complexity O(n), Space Complexity O(1)
        """
        F = [0, 1]
        if n < 2:
            return F[n]
        for i in range(2, n+1):
            F_i = sum(F) # implementation of the recurrence relation: Fn = Fn-2 + Fn-1
            F[:] = F[1:] + [F_i] # shift to prepare for the next iteration
        return F_i

>>> F.top_down(10)
55
>>> F.bottom_up(10)
55
