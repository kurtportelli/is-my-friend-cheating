def removNb(n):
    result = []
    total = sum(range(1, n+1))
    for a in range(1, n+1):
        b = (total - a) / (a + 1)
        if b == int(b) and b < n:
            result.append((a, int(b)))
    return result
