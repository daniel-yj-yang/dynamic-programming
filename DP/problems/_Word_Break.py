# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from typing import List
from functools import lru_cache
import inspect


class Word_Break():

    def explanation(self):
        print(f"\nThe question provides a string called \"s\" and a list called \"wordDict\", and asks to check whether s can be fully segmented by one or more dictionary words.")
        print(f"\nThe recurrence relation:\n")
        print(f"If a string is segmentable, if must be true that \"the string\" = \"part 1\" + \"a word from the wordDict\", and importantly \"part 1\" must be segmentable as well.\n")
        print(f"For example, s = \"codingisfun\", wordDict = ['coding', 'is', 'fun']; it follows that \"codingisfun\" = \"codingis\" + \"fun\"; and then \"codingis\" = \"coding\" + \"is\"; and then \"coding\" = \"\" + \"coding\".\n")
        print(f"Therefore, conceptually we can define a boolean function called segmentable(length), which is True if s[0:length] is segmentable by the words in wordDict.\n")
        print(f"Implementation: segmentable(length) = segmentable(length-len(word)) & whether s[length-len(word):length] is in wordDict, for one of the words (the choice) in wordDict;\n")
        print(inspect.getsource(self.top_down) + '\n')
        print(inspect.getsource(self.bottom_up))

    def top_down(self, s: str = "codingisfunpythonisgreat", wordDict: List[str] = ["coding", "is", "fun", "python", "great"]) -> bool:
        """
        Typically, Recursion + Memoization; Time Complexity O(n), Space Complexity O(n) for the recursion call stack;
        In this question, using hashset, Time Complexity O(len(s) * len(wordDict)), Space Complexity O(len(s) + len(wordDict));
        """
        wordset = set(wordDict)
        wordlens = [len(word) for word in wordset]
        @lru_cache(maxsize=None)
        def segmentable(length: int): # whether s[0:length] is segmentable by the words in wordDict
            if length == 0:
                return True
            for wordlen in wordlens:
                part1_length = length - wordlen
                if part1_length >= 0:
                    if segmentable(part1_length) and s[part1_length:length] in wordset:
                        return True
            return False
        return segmentable(len(s))

    def bottom_up(self, s: str = "codingisfunpythonisgreat", wordDict: List[str] = ["coding", "is", "fun", "python", "great"]) -> bool:
        """
        Typically, tabulation - full tabulation has Space Complexity O(n); keeping only needed items has Space Complexity O(1);
        In this question, using hashset, Time Complexity O(len(s) * len(wordDict)), Space Complexity O(len(s) + len(wordDict));
        """
        wordset = set(wordDict)
        wordlens = [len(word) for word in wordset]
        segmentable = [False] * (len(s)+1) # segmentable[length] is True if s[0:length] is segmentable by the words in wordDict
        segmentable[0] = True
        for length in range(1, len(s)+1):
            for wordlen in wordlens:
                part1_length = length - wordlen
                if part1_length >= 0:
                    if segmentable[part1_length] and s[part1_length:length] in wordset:
                        segmentable[length] = True
                        break
        return segmentable[len(s)]
        
