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

Installation
------------

.. code-block::

   pip install DynamicProgramming


Sample Usage
------------

>>> from DP import Fibonacci_numbers as fib
>>> fib()
1. recurrence relation (subproblem): Fn = Fn-1 + Fn-2
2. bottom-up DP; Time Complexity O(n), Space Complexity O(1)

```
def fib(n):
    F = [0, 1]    
    if n < 2:
        return F[n]
    for i in range(2, n+1):
        F_i = sum(F) # implementation of the recurrence relation: Fn = Fn-1 + Fn-2
        F[:] = F[1:] + [F_i]
    return F_i
)
```