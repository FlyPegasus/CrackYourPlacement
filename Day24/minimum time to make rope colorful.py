class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) <= 1:
            return 0
        i = 1
        ttime = 0
        while i < len(neededTime):
            if colors[i] == colors[i - 1]:
                #print(colors)
                if neededTime[i - 1] < neededTime[i]:
                    colors = colors[:i - 1] + colors[i:]
                    ttime += neededTime[i - 1]
                    del neededTime[i - 1]
                else:
                    colors = colors[:i] + colors[i + 1:]
                    ttime += neededTime[i]
                    del neededTime[i]
            else:
                i += 1
        return ttime