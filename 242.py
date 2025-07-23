'''
242. Valid Anagram
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # OnlogN time complexity
        # if sorted(s) == sorted(t):
        #     return True
        # return False

        # O(N) time complexity:
        hashmap = {}
        hashmap1 = {}

        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            if c in hashmap:
                hashmap[c]+=1
        for ch in t:
            if ch not in hashmap1:
                hashmap1[ch] = 1
            if ch in hashmap1:
                hashmap1[ch] += 1

        return len(hashmap) == len(hashmap1) and hashmap.items() == hashmap1.items()