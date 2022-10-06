#CHANGE

s = ["aabbaac", "lkmn"]
t = ["baacccb", "dddd"]
arr= []

for i in range(len(s)):
    ds = {}
    dt = {}
    difference = 0
    for j in range(len(s[i])):
        if s[i][j] not in ds:
            ds[s[i][j]] = 1
        else:
            ds[s[i][j]] = ds.get(s[i][j]) + 1

    for k in range(len(s[i])):
        if t[i][k] not in dt:
            dt[t[i][k]] = 1
        else:
            dt[t[i][k]] = dt.get(t[i][k]) + 1

    
    for x in range(len(s[i])):
        if t[i][x] in ds:
            difference = abs(ds[t[i][x]] - dt[t[i][x]])
        else:
            difference += 1

    if difference > 3:
        arr.append("NO")
    else:
        arr.append("YES")

print(arr)

