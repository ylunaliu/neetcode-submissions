class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        current_window = set()
        max_length = 0
        for right, ch in enumerate(s):
            while ch in current_window:
                current_window.remove(s[left])
                left+=1
            current_window.add(ch)
            length = right-left+1
            max_length = max(length, max_length)
        return max_length
