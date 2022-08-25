def height(t):
    if is_leaf(t):
        return 0
    else:
        return max(height(b) for b in branches(t))+1
      
def max_path_sum(t):
    if is_leaf(t):
        return label(t)
    else:
        return label(t)+max(max_path_sum(b) for b in branches(t))
      
      
      
def square_tree(t):
    if is_leaf(t):
        return tree(label(t)**2)
    else:
        return tree(label(t)**2,[square_tree(b) for b in branches(t)])
      
      
def find_path(tree, x):
    if label(tree)==x:
        return [label(tree)]
    for b in branches(tree):
        path=find_path(b,x)
        if path:
            return [label(tree)]+path
          
def prune_binary(t, nums):
    if is_leaf(t):
        if str(label(t)) in nums:
            return t
        return None
    else:
        next_valid_nums =[n[1:] for n in nums if str(label(t))==n[0]]
        new_branches = []
    for b in branches(t):
        pruned_branch = prune_binary(b, next_valid_nums)
        if pruned_branch is not None:
            new_branches = new_branches + [pruned_branch]
    if not new_branches:
        return None
    return tree(label(t),new_branches)
