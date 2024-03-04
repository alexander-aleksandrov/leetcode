"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    i = 0
    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            area = heights[top] * ((i - stack[-1] - 1) if stack else i)
            max_area = max(max_area, area)
    while stack:
        top = stack.pop()
        area = heights[top] * ((i - stack[-1] - 1) if stack else i)
        max_area = max(max_area, area)
    return max_area
