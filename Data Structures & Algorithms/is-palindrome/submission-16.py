class Solution:
    def isPalindrome(self, s: str) -> bool:
        #First need to remove all spaces
        #Divide into two string? 
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        print(len(s))
        if len(s)%2==0:
            upper = s[0:len(s)//2]
            lower = s[len(s)//2:]
        else:
            upper = s[0:len(s)//2]
            lower = s[len(s)//2+1:]
        lower_r = lower[::-1]
        print(upper, lower)
        for i in range(len(upper)):
            if(upper[i]!=lower_r[i]):
                return False
        return True