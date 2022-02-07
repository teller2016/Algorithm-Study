# https://leetcode.com/problems/palindrome-pairs/

##### 이해 못함 #####

# 타임 아웃 - 브루트 포스
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def is_palindrome(word):
            return word == word[::-1]

        output = []

        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i, j])

        return output