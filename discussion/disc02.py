

def print_delayed(x):
    def p(y):
        print(x)
        return print_delayed(y)
    return p
