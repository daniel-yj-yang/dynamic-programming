# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from functools import lru_cache
import inspect


class Coin_Change():

    # For recurrence relation, see also slide #6 of http://www.columbia.edu/~cs2035/courses/csor4231.S19/dynamic.pdf

    def explanation(self):
        print(f"\nThe question provides a coins array for the different denominations of the coins and an integer amount, and asks you to return the minimal number of coins needed to make up that amount, or -1 if not possible to make up.")
        print(f"\nThe recurrence relation:\n")
        print(f"F(amount_left) = min([ F(amount_left - coin) + 1 for coin in coins if (amount_left - coin) >= 0 ]), which means using 1 of the coins (the choice) toward making up the amount, where F(x) is the minimal number of coins needed to make up the amount of x, and F(0) = 0, and \"+ 1\" means using 1 more coin.\n")
        print(inspect.getsource(self.top_down) + '\n')
        print(inspect.getsource(self.bottom_up))

    def top_down(self, coins=[1, 5, 10, 25], amount=150):
        """
        Recursion + Memoization;
        Time Complexity O(n), Space Complexity O(n) for the recursion call stack;
        """
        @lru_cache(maxsize=None)
        def dp(amount_left):
            if amount_left == 0:
                return 0
            children = [dp(amount_left-coin)+1 for coin in coins if (amount_left-coin)>=0]
            if children:
                return min(children)
            else:
                return float('inf')
        return dp(amount) if dp(amount) != float('inf') else -1

    def bottom_up(self, coins=[1, 5, 10, 25], amount=150):
        """
        Tabulation - full tabulation has Space Complexity O(n); keeping only needed items has Space Complexity O(1);
        Time Complexity O(n), Space Complexity O(1);
        """
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for amount_left in range(min(coins), amount+1):
            children = [dp[(amount_left-coin)]+1 for coin in coins if (amount_left-coin)>=0]
            if children:
                dp[amount_left] = min(children)
        return dp[amount] if dp[amount] != float('inf') else -1
