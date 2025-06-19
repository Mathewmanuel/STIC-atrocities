print("Hi")
def multipleitems(*args):
    print(args)
    print(type(args))

multipleitems("Dave","John","sara")

def mulkwargs(**kwargs):
    print(kwargs)
    print(kwargs)
    print(type(kwargs))

mulkwargs(first="Dave",last="gray")