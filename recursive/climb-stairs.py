
def climbStairs(self, n: int) -> int:
    mem_ways = []
    for i in range(0, n+1):
        if i <= 2:
            mem_ways.append(i)
        else:
            mem_ways.append(mem_ways[i-1] + mem_ways[i-2])
    return mem_ways[n]
