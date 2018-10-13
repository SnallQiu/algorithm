#类装饰器（decorator） python cookbook p286
#其中有用到 描述符 这篇博客很nb  https://blog.csdn.net/sjyttkl/article/details/80655421

#总结下描述符类的规律
#对于obj.attr 如果不是自动属性，则先找到obj.__class__.__dict__ 如果attr存在并且是一个data descriptor(有__set__方法)，则执行__get__方法
class Descriptor:
    def __init__(self,name=None,**opts):
        self.name = name
        for key,values in opts.items():
            setattr(self,key,values)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

def Typed(expected_type,cls=None):
    if cls is None:
        return lambda cls:Typed(expected_type,cls)#????
    super_set = cls.__set__
    #重写__set__方法，加入type判断
    def __set__(self,instance,value):
        if not isinstance(value,expected_type):
            raise TypeError('excepted '+str(expected_type))
        super_set(self,instance,value)
    cls.__set__ = __set__
    return cls
@Typed(int)
class Integer(Descriptor):
    pass

class Stock:
    price = Integer('price')
    def __init__(self,price):
        self.price = price
if __name__ == '__main__':
    stock = Stock(1)
    print (stock.__class__.__dict__)