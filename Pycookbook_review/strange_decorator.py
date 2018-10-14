def Type(a,cls=None):
    if cls is None:
        return lambda cls:Type(a,cls)
    print (a)
    return cls

@Type('hello world')
class Test:
    pass

test = Test()
