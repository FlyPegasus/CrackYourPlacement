class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        j = 0
        for i in strs:
            if j == 0:
                longest_prefix = i
                j += 1
            else:
                ind = 0
                while ind < len(i) and ind < len(longest_prefix):
                    if i[ind] == longest_prefix[ind]:
                        ind += 1
                    else:
                        break
                temp = longest_prefix[:ind]
                longest_prefix = temp
        return longest_prefix