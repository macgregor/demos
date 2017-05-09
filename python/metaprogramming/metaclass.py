import sys
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

class MyMeta(type):
    def __new__(meta, name, bases, dct):
        print('-----------------------------------')
        print("Allocating memory for class", name)
        print(meta)
        print(bases)
        print(dct)
        return super(MyMeta, meta).__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('-----------------------------------')
        print("Initializing class", name)
        print(cls)
        print(bases)
        print(dct)
        super(MyMeta, cls).__init__(name, bases, dct)

    def __call__(cls, *args, **kwds):
        print('__call__ of ', str(cls))
        print('__call__ *args=', str(args))
        return type.__call__(cls, *args, **kwds)

if PY2:
    class MyPy2Klass(object):
        __metaclass__ = MyMeta

        def __init__(self, a, b):
            print('MyPy2Klass object with a=%s, b=%s' % (a, b))

    print('gonna create foo now...')
    foo = MyPy2Klass(1, 2)
elif PY3:
    '''
    class MyPy3Klass(object, metaclass=MyMeta):... is the python 3 way of doing
    but this causes a SyntaxError when run in python 2. The future package provides
    a python 2/3 compatible alternative, with_metaclass.

    Be sure to sudo pip install future
    '''
    from future.utils import with_metaclass
    class MyPy3Klass(with_metaclass(MyMeta, object)):

        def __init__(self, a, b):
            print('MyPy3Klass object with a=%s, b=%s' % (a, b))

    print('gonna create foo now...')
    foo = MyPy3Klass(1, 2)
