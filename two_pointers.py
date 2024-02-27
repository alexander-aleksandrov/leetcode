def target_sum(arr, target):
    current_sum  = 0 
    left = 0 
    right = len(arr) - 1
    while left != right:
        current_sum  = arr[left] + arr[right]
        if current_sum < target:
            left +=1 
        elif current_sum > target:
            right -=1
        else:
            return arr[left], arr[right]
    else:
        return None
    
def container_with_most_water(lines_heights):
    current_area  = 0 
    max_arrea = 0 
    left = 0
    right = len(lines_heights) - 1
    while left != right:
        current_area = (right+1 - left) * min(lines_heights[left], lines_heights[right])
        max_arrea = max(current_area, max_arrea)
        if lines_heights[left] < lines_heights[right]:
            left +=1
        else:
            right-=1
    return max_arrea

def main():
    arr = [1, 3, 2, 4, 3]
    target = 6 
    print(container_with_most_water(arr))


main()