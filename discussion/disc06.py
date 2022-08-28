def memory(n):
    def f(g):
        nonlocal n
        n=g(n)
        return n
    return f
  
def group_by(s, fn):
    grouped = {}
    for i in s:
        key = fn(i)
        if key in grouped.keys():
            grouped[key].append(i)
        else:
            grouped[key] = [i]
    return grouped
  
  
def add_this_many(x, el, s):
    count=0
    for i in s:
        if i==x:
            count+=1
    for i in range(count):
        s.append(el)
    return s
  
  
  def filter(iterable, fn):
    for i in iterable:
        if fn(i):
            yield i
            
  def merge(a, b):
    r1 = next(a)
    r2 = next(b)
    while True:
        if r1==r2:
            yield r1
            r1=next(a)
            r2=next(b)
        elif r1>r2:
            yield r2
            r2=next(b)
        else:
            yield r1
            r1=next(a)
