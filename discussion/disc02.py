def keep_ints(cond, n):
    t=1
    while t<=n:
        if(cond(t)):
            print(t)
        t += 1
        
def make_keeper(n):
    def do(cond):
        t = 1
        while t <= n:
            if (cond(t)):
                print(t)
            t += 1
    return do
