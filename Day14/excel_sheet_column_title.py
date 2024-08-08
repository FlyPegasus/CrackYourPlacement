class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = "xABCDEFGHIJKLMNOPQRSTUVWXYZ"
        t = columnNumber
        stk = []
        ans = ""
        while t > 26:
            if t%26 == 0:
                stk.append(26)
                t = t//26 - 1
            else:
                stk.append(t%26)
                t //= 26
        ans += s[t]
        #print(stk)
        while len(stk) > 0:
            ans += s[stk.pop()]
        return ans