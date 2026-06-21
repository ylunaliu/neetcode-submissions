class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count_s1 = {}
        count_s2 = {}
        window_size = len(s1)
        left = 0

        for ch in s1:
            count_s1[ch] = count_s1.get(ch, 0) + 1

        for right in range(len(s2)):
            ch = s2[right]
            count_s2[ch] = count_s2.get(ch, 0) + 1

            if right - left + 1 > window_size:
                left_ch = s2[left]
                count_s2[left_ch] -= 1

                if count_s2[left_ch] == 0:
                    del count_s2[left_ch]

                left += 1

            if count_s1 == count_s2:
                return True

        return False