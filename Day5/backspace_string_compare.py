class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk1 = []
        stk2 = []
        for i in s:
            if i == '#':
                if  len(stk1) != 0:
                    stk1.pop()
            else:
                stk1.append(i)
        for i in t:
            if i == '#':
                if len(stk2) != 0:
                    stk2.pop()
            else:
                stk2.append(i)
        print(stk1)
        print(stk2)
        if len(stk1) != len(stk2):
            return False
        for j in range(len(stk1)):
            if stk1[j] != stk2[j]:
                return False
        return True