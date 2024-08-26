class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        last = len(height) - 1
        area = 0
        while start < last:
            t = (last - start) * min(height[start], height[last])
            if t > area:
                area = t
            if height[start] < height[last]:
                start += 1
            else:
                last -= 1
        return area