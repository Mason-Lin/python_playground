import enum

class X(enum.Enum):
    a = 1
    b = 2

    @classmethod
    def foo(self):
        print('ccc')

if __name__ == "__main__":
    z = X['a']
    print(X.a)
    print(z)
    X.foo()
    z.foo()
