#CHANGE

s = ["aabbaac", "kldhdjd", "lkmn"]
t = ["baacccb", "sd", "dddd"]
arr= []

for i in range(len(s)):
    ds = {}
    dt = {}
    difference = 0

    if len(s[i]) != len(t[i]):
        arr.append("NO")
        continue

    #loop thorugh letters in the s array and count all of their occurences
    for j in range(len(s[i])):
        if s[i][j] not in ds:
            ds[s[i][j]] = 1
        else:
            ds[s[i][j]] = ds.get(s[i][j]) + 1

    #loop thorugh letters in the t array and count all of their occurences
    for k in range(len(s[i])):
        if t[i][k] not in dt:
            dt[t[i][k]] = 1
        else:
            dt[t[i][k]] = dt.get(t[i][k]) + 1

    #Loop through the word a final time and compare the dictionries while counting the letter differences
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

