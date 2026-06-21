class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1
        
        count_s = {}
        left = 0
        shortest_substring_length = float('inf')
        ans = [-1,-1]
        for right, ch in enumerate(s):
            # update the current window
            count_s[ch] = count_s.get(ch, 0) +1
            while(self.contains(count_s, count_t)):
                if (right-left+1)< shortest_substring_length:
                    shortest_substring_length = right-left+1
                    ans = [left, right]
                    if count_s[s[left]] == 0:
                        del count_s[s[left]]
                count_s[s[left]]-=1
                left +=1
        if ans==[-1,-1]:
            return ""

        return s[ans[0]:ans[1]+1]
            # we only strink it if the count_s contains at least count_t
    
    def contains(self, count_s, count_t):
        for ch in count_t:
            if count_s.get(ch, 0) < count_t[ch]:
                return False
        return True

