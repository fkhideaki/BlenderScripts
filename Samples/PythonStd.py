import inspect


def intToString(int_val):
    return str(int_val)

def printObjectInfo(obj):
    dir(obj)

# メンバ一覧表示
def pdir(obj):
    for s in dir(obj):
        print(s)

# 型名表示
def printType(obj):
    print(type(obj))

# 関数の引数リストを表示
def printArgs(func):
    print(inspect.getargspec(func))
