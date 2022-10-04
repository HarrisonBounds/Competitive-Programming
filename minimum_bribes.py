#NEW YEAR CHAOS

def minimumBribes(q):
    total_bribes = 0
    
    for i in range(len(q) - 1, 0, -1):
        if q[i] != i + 1:
            if q[i - 1] == i + 1:
                total_bribes += 1
                q[i - 1], q[i] = q[i], q[i - 1]
            elif q[i - 2] == i + 1:
                total_bribes += 2
                q[i - 2], q[i - 1], q[i] = q[i - 1], q[i], q[i - 2] #fancy way of switiching indexes in python
            else:
                print("Too chaotic")
                return
            
    print(total_bribes)
            