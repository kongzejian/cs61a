def sum_nums(lnk):
    if lnk is Link.empty:
        return 0
    else:
        return lnk.first+sum_nums(lnk.rest)
      
def multiply_lnks(lst_of_lnks):
    cur_result=1
    next=[]
    for i in lst_of_lnks:
        if i is Link.empty:
            return Link.empty
        cur_result*=i.first
        next.append(i.rest)
    return Link(cur_result,multiply_lnks(next))
  
  
def flip_two(lnk):
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    else:
        lnk.first,lnk.rest.first=lnk.rest.first,lnk.first
        flip_two(lnk.rest.rest)
        
        
def filter_link(link, f):
    while not link is Link.empty:
        if f(link.first):
            yield link.first
        link=link.rest
        
        
def make_even(t):
    if t.is_leaf():
        if t.label%2==1:
            t.label += 1
        return
    else:
        if t.label%2==1:
            t.label+=1
        for b in t.branches:
            make_even(b)
            
            
            
def square_tree(t):
    t.label=t.label**2
    for b in t.branches:
        square_tree(b)  
        
        
def find_paths(t, entry):
    paths = []
    if t.label==entry:
        paths.append([t.label])
    for b in t.branches:
        branch_path=[[t.label]+ path for path in find_paths(b,entry)]
        paths+=(branch_path)
    return paths
  
  
def combine_tree(t1, t2, combiner):
    if t1.is_leaf():
        return Tree(combiner(t1.label,t2.label))
    else:
        return Tree(combiner(t1.label,t2.label),[combine_tree(a,b,combiner) for a,b in zip(t1.branches,t2.branches)])
            
            
 def alt_tree_map(t, map_fn):
        t.label=map_fn(t.label)
        for b in t.branches:
            alt_tree_map(b,map_fn)
    
