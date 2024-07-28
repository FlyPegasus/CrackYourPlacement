class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        stk = []
        temp = 0
        while i > -1 and j > -1:
            f1 = int(a[i])
            f2 = int(b[j])
            val = (f1 + f2 + temp) % 2
            stk.append(val)
            temp = (f1 + f2 + temp) // 2
            i -= 1
            j -= 1
        while i > -1:
            f1 = int(a[i])
            val = (f1 + temp) % 2
            stk.append(val)
            temp = (f1 + temp) // 2
            i -= 1
        while j > -1:
            f1 = int(b[j])
            val = (f1 + temp) % 2
            stk.append(val)
            temp = (f1 + temp) // 2
            j -= 1
        if temp == 1:
            stk.append(temp)
        ans = ""
        while(len(stk) != 0):
            ans += str(stk.pop())
        return ans