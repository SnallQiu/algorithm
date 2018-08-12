
class Test1:
    f=open('/Users/qiu/Desktop/my_pycham_project/algorithm/Pycookbook_review/Node.py','r')
    '''这里yield from 将f这个可迭代对象作为一个generator,当后面调用这个函数的时候，他会将这个生产者产生的东西传递给函数。'''

    def read_file(self):
        yield from self.f

    def __init__(self):
        for s in self.read_file():
            print(s)

test1=Test1()


from collections import Iterable
class Test2:
    '''yield 在递归中的应用'''
    a = [1,2,[3,4,[5,6,[7,8],9,]],10]
    def __init__(self):
        for out in self.run(self.a):
            print (out)

    def run(self,a,ignore_types=(str,bytes)):

        for i in a:
            if isinstance(i,Iterable) and not isinstance(i,ignore_types):
                yield from self.run(i)
            else:
                yield i

test2 = Test2()
