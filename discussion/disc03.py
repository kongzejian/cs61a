def multiply(m, n):
    if(m==0):
        return 0
    return multiply(m-1,n)+n
  
  
  def hailstone(n):
    print(n)
    if n==1:
        return 1
    if n%2==0:
        n=n//2
        return hailstone(n)+1
    else:
        n=3*n+1
        return hailstone(n)+1
      
def merge(n1, n2): 
    if(n1==0):
        return n2
    if(n2==0):
        return n1
    m=n1%10 
    n=n2%10 
    if(m<n):
        n1=n1//10 
        return merge(n1,n2)*10+m
    else:
        n2=n2//10
        return merge(n1,n2)*10+n
      
      
def make_func_repeater(f, x):
    def repeat(y):
        if y==0:
            return x
        else:
            return f(repeat(y-1))
    return repeat
  
  
  
def is_prime(n):
    def prime_helper(x):
        if n==x:
            return True
        elif n%x==0 or n==1:
            return False
        else:
            return prime_helper(x+1)
    return prime_helper(2)
