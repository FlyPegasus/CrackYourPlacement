class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in range(len(s)):
            if s[i] in ('(', '{', '['):
                stk.append(s[i])
            else:
                #print(stk)
                if len(stk) < 1:
                    return False
                flag = 1
                if s[i] == ')' and stk[-1] == '(':
                    stk.pop()
                    flag = 0
                if s[i] == '}' and stk[-1] == '{':
                    stk.pop()
                    flag = 0
                if s[i] == ']' and stk[-1] == '[':
                    stk.pop()
                    flag = 0
                if flag == 1:
                    return False
        if len(stk) > 0:
            return False        
        return True