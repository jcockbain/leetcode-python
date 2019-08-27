def maxIncreaseKeepingSkyline(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    rowMaxes = []
    colMaxes = []
    diff = 0
    for row in grid:
        rowMaxes.append(max(row))
        for j in range(len(row)):
            if len(colMaxes) <= j:
                colMaxes.append(row[j])
            else:
                if row[j] > colMaxes[j]:
                    colMaxes[j] = row[j]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            diff += min(rowMaxes[i], colMaxes[j]) - grid[i][j]
    return diff
