#creates a class (not an instance) from the provided keyword args
#each keyword becomes a class attribute (added to self on instantiation)
def make_myklass(**kwattrs):
    return type('MyKlass', (object,), dict(**kwattrs))

myklass_foo_bar = make_myklass(foo=2, bar=4)
print(myklass_foo_bar)

instance = myklass_foo_bar()
print(instance)
print(instance.foo, instance.bar)

#I wonder if we can subclass this monstrosity...
def make_subklass(**kwattrs):
    return type('MySubklass', (myklass_foo_bar,), dict(**kwattrs))

mysubklass_baz = make_subklass(baz='theres no way this will work')
baz = mysubklass_baz()
print(baz.foo, baz.bar, baz.baz)

print('python is nuts, man')
