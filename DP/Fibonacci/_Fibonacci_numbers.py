# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


def Fibonacci_numbers():
  print("1. recurrence relation (subproblem): Fn = Fn-1 + Fn-2")
  print("2. Bottom-up DP, Time Complexity O(n)")
  print("""
def fib(n):
    F = [0, 1]    
    if n < 2:
        return F[n]
    for i in range(2, n+1):
        F_i = sum(F)
        F[:] = F[1:] + [F_i]
    return F_i
)""")

