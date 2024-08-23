class Solution:
    def minDeletions(self, s: str) -> int:
        stk = dict()
        for i in range(len(s)):
            if s[i] in stk:
                stk[s[i]] += 1
            else:
                stk[s[i]] = 1
        #print(stk)
        lst = []
        for key in stk:
            lst.append(stk[key])
        lst.sort()
        lst.reverse()
        #print(lst)
        flag = 1
        count = 0
        while flag == 1:
            flag = 0
            for i in range(len(lst) - 1):
                if lst[i] == lst[i + 1] and lst[i] != 0:
                    flag = 1
                    count += 1
                    lst[i + 1] -= 1
            #flag = 0
            lst.sort()
            lst.reverse()
        #print(lst)
        return count