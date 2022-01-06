# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from functools import lru_cache
import inspect


class Decode_Ways():

    def explanation(self):
        print(f"\nWhile the uppercase letters 'A' ~ 'Z' are encoded to be '1' ~ '26', the question provides a string of numbers (e.g., '9257') and asks to return the number of unique ways to decode that string to letters (e.g., 'IBEG' and 'IYG'; thus 2 ways here).")
        print(f"\nThe recurrence relation:\n")
        print(f"n_ways_to_decode(substr_to_the_right) = n_ways_to_decode(substr_to_the_right[1:]) + n_ways_to_decode(substr_to_the_right[2:]), with a choice between making a single-digit vs. double-digit decoding.\n")
        print(f"However, there are some boundary conditions that would invalidate this relation and need to be handled first, including:\n")
        print(f"1. When the substr has no character and is \"\", it means the decoding process in that path has successfully completed and should return 1 as the # of decoding way in that path.\n")
        print(f"2. When the substr has just 1 char and it's \"0\", it means it cannot be decoded any further in that path and should return 0 as the # of decoding way in that path.\n")
        print(f"3. When the substr has just 1 char and it's other than \"0\", it means the decoding process in that path can be successfully completed and should return 1 as the # of decoding way in that path.\n")
        print(f"4. When the substr's first two chars have a numeric integer value greater than 26, it means double-digit decoding would not work and thus proceed with only single-digit decoding.\n")
        print(inspect.getsource(self.top_down) + '\n')
        print(inspect.getsource(self.bottom_up))

    def top_down(self, s: str = "11106") -> int:
        """
        Typically, Recursion + Memoization; Time Complexity O(n), Space Complexity O(n) for the recursion call stack;
        """
        @lru_cache(maxsize=None)
        def decode_ways(substr):  # return number of decode ways
            if not substr:
                return 1
            elif substr[0] == '0':
                return 0
            elif len(substr) == 1:
                return 1
            elif int(substr[0:2]) > 26:
                return decode_ways(substr[1:])
            else:
                return decode_ways(substr[1:]) + decode_ways(substr[2:])
        return decode_ways(s)

    def bottom_up(self, s: str = "11106") -> int:
        """
        Typically, tabulation - full tabulation has Space Complexity O(n); keeping only needed items has Space Complexity O(1);
        In this question, using a single for loop and a hashmap, Time Complexity O(len(s));
        """
        decode_ways = {} # key: remaining substr to the right: value: number of decode ways
        decode_ways[""] = 1
        for start_idx in range(len(s)-1, -1, -1):
            substr = s[start_idx:]
            if substr[0] == '0':
                decode_ways[substr] = 0
            elif len(substr) == 1:
                decode_ways[substr] = 1
            elif int(substr[0:2]) > 26:
                decode_ways[substr] = decode_ways[substr[1:]]
            else:
                decode_ways[substr] = decode_ways[substr[1:]] + decode_ways[substr[2:]]
        return decode_ways[s]
        
