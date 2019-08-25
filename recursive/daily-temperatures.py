# Time O(NW)
# Space O(N + W)


def dailyTemperatures(T):
    nxt = [float('inf')] * 102
    ans = [0] * len(T)
    for i in range(len(T) - 1, -1, -1):
        warmer_index = min(nxt[t] for t in range(T[i]+1, 102))
        if warmer_index < float('inf'):
            ans[i] = warmer_index - i
        nxt[T[i]] = i
    return ans

# Time O(N)
# Space O(W)


def dailyTemperatures2(T):
    ans = [0] * len(T)
    stack = []  # indexes from hottest to coldest
    for i in range(len(T) - 1, -1, -1):
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] - i
        stack.append(i)
    return ans


print(dailyTemperatures([10, 20, 15, 28, 12, 17]))
