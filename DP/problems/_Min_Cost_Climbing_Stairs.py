# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from functools import lru_cache
import inspect


class Min_Cost_Climbing_Stairs():

    def explanation(self):
        print(f"\nThe question provides you an integer array cost for the cost of i-th step you must pay on a staircase, and asks you to return the minimum cost to reach the top of the floor, while you may start at 0-th or 1-th step, and take 1 or 2 steps afterward at every choice.")
        print(f"\nThe recurrence relation: f(i) = cost[i] + min( f(i-2), f(i-1) ), which means in order to reach to the i-th step, there was a choice between (having taken two steps to get there and assumed all the min. cost two steps back) vs. (having taken one step to get there and assumed all the min. cost one step back), where f(i) is the min. cost climbing to the i-th step, with f(0) = cost[0], f(1) = cost[1]\n\nSource codes:\n")
        print(inspect.getsource(self.top_down) + '\n')
        print(inspect.getsource(self.bottom_up))

    def top_down(self, cost = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]): # demo cost array
        """
        Recursion + Memoization;
        Time Complexity O(n), Space Complexity O(n) for the recursion call stack
        """
        cost.append(0) # the question asks to find out the minimum cost to reach the top of the floor, and there is no inherent cost there
        @lru_cache(maxsize=None)
        def mincost(i):
            if i <= 1:
                return cost[i] # one may either start from the 0-th step, or the 1-th step 
            return cost[i] + min( mincost(i-2), mincost(i-1) )
        return mincost(len(cost)-1)

    def bottom_up(self, cost = [3, 10, 3, 1, 2, 4, 10, 2, 44, 98]):  # demo cost array
        """
        Tabulation - full tabulation has Space Complexity O(n); keeping only needed items has Space Complexity O(1)
        Time Complexity O(n), Space Complexity O(1)
        """
        cost.append(0) # the question asks to find out the minimum cost to reach the top of the floor, and there is no inherent cost there
        mincost_i_minus_2, mincost_i_minus_1 = cost[0], cost[1]
        for i in range(2, len(cost)): # the i-th step
            mincost_i = cost[i] + min( mincost_i_minus_2, mincost_i_minus_1 ) # implementation of the recurrence relation: f(i) = cost[i] + min( f(i-2), f(i-1) )
            mincost_i_minus_2, mincost_i_minus_1 = mincost_i_minus_1, mincost_i  # shift to prepare for the next iteration
        return mincost_i # mincost_i: the min. cost to reach the top floor, i is 0th-indexed

