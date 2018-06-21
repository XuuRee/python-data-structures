def beg(arr):
    a = []
    b = []
    c = []

    for i in arr:
        if i == 0:
            a.append(i)
        if i == 1:
            b.append(i)
        if i == 2:
            c.append(i)
    return a+b+c


a = []
b = [0,0,0]
c = [1,2,1,1,2,1,2]
d = [0,2,1,0,1,0,2,2,2,1,0,2,1,0,1,2,0]

print(beg(a))
print(beg(b))
print(beg(c))
print(beg(d))