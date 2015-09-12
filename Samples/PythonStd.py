import inspect


def IntToString(int_val):
    return str(int_val)

def PrintObjectInfo(obj):
    dir(obj)

def pdir(obj):
    print(dir(obj))

def pdirl(obj):
    for s in dir(obj):
        print(s)

def ptype(obj):
    print(type(obj))

def print_args(func):
    print(inspect.getargspec(func))
