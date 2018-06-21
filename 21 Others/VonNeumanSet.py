def vonNoeman(n):
    if n == 0:
        return []
    res = []
    for i in range(n,0,-1):
        res.append(vonNoeman(n-i))
    return res

print(vonNoeman(30))