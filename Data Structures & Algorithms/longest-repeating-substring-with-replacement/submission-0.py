class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = 0
        count = {} #key is the letter, value is the frequency
        # I should use sliding window
        # Add character to dic, if the next ch is different than the previous character
        # update the frequency in the sliding window and see if replace the less frequent
        # character less than k times will give the maximum length
        # move left if it cannot be done
        for right, ch in enumerate(s):
            # Need to initilize the count
            if ch not in count:
                count[ch]=0
            count[ch] +=1
            while((right-left+1) - max(count.values())>k):
                count[s[left]] -=1
                left +=1
            max_length = max(max_length, right-left+1)
        return max_length
            