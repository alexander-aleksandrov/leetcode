def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key = lambda x: x[0] )
    merged_intervals = [intervals[0]]
    for start, end in intervals[1:]: 
        prev_end = merged_intervals[-1][1]
        if start <= prev_end:
            merged_intervals[-1][1] = max(end, prev_end)
        else:
            merged_intervals.append([start, end])
    return merged_intervals

def intersect(intervals):
    if not intervals:
        return []
    intervals.sort(key = lambda x: x[0])
    intersection = [intervals[0]]
    for start, end in intervals[1:]:
        prev_start = intersection[-1][0]
        prev_end = intersection[-1][1]
        if start > prev_start and start < prev_end:
            intersection[-1][0]  = max(start, prev_start)
            intersection[-1][1]  = min(end, prev_end)
        else:
            intersection.append([start, end])
    return intersection



def main():
    print(intersect([[1,3],[2,6],[8,13],[9,18]]))
    print(intersect([[1,4],[4,5]]))
    

if __name__ == "__main__":
    main()