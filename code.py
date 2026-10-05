class Solution:
    def maxPower(self, s: str) -> int:
        n=len(s)
        c=1
        m=0
        
        for i in range(1,n):
            if i<n and s[i-1]==s[i]:
                c+=1
            else:
                m=max(m,c)
                c=1
        return max(m,c)

        
