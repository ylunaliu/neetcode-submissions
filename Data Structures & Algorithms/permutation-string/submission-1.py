class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s2 is always longer than s1, if not return false
        if(len(s2)<len(s1)):
            return False
        count_s1 = {}
        for s in s1:
            if s not in count_s1:
                count_s1[s] = 0
            count_s1[s]+=1
        print(count_s1)
        
        left =0
        count_s2 = {}
        window_size = len(s1)-1
        for right in range(len(s2)):
            if s2[right] not in count_s2:
                count_s2[s2[right]]=0
            count_s2[s2[right]]+=1
            print(count_s2)
            if count_s2==count_s1:
                return True
            if (right-left+1)>window_size:
                count_s2[s2[left]]-=1
                count_s2 = {k: v for k, v in count_s2.items() if v != 0}
                left+=1
        return False
