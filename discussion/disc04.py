def count_stair_ways(n):
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        total=0
        for i in range(1,3):
            total+=count_stair_ways(n-i)
    return total
      
      
def count_k(n, k):
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        i=1
        total=0
        while(i<=k):
            total+=count_k(n-i,min(k,n-i))
            i+=1
        return total
      
      
def even_weighted(s):
    return [s[i]* i for i in range(len(s) if i%2==0)]
  
  

  def max_product(s):
    if s==[]:
        return 1
    elif len(s)==1:
        return s[0]
    else:
        return max(s[0]*max_product(s[2:]),max_product(s[1:]))
