class Base:
    def __init__(self):
        self._protected_var = 5

class Derived(Base):
    def __init__(self):
        Base.__init__(self)

class SubDerived(Derived):
    def __init__(self):
        Derived.__init__(self)

obj = SubDerived()
print(obj._protected_var)
# result = 5