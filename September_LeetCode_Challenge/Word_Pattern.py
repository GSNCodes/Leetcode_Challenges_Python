Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between 
a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, 
and str contains lowercase letters that may be separated by a single space.



# My Solution
# O(n - no.of words/chars) Time and O(m - no. of unique words/chars)
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        mappings = dict()
        word_list = str.split()
        if len(set(word_list)) != len(set(pattern)) or len(pattern) != len(word_list):
            return False
        
        for i, word in enumerate(word_list):
            if word in mappings:
                if mappings[word] != pattern[i]:
                    return False
                
            else:
                mappings[word] = pattern[i]
        
        return True

# O(n - no.of words/chars) Time and O(m - no. of unique words/chars)
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_char = {}
        map_word = {}
        
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c not in map_char:
                if w in map_word:
                    return False
                else:
                    map_char[c] = w
                    map_word[w] = c
            else:
                if map_char[c] != w:
                    return False
        return True