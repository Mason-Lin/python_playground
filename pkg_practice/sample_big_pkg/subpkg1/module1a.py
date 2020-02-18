# absolute import
# from sample_big_pkg.subpkg1 import module1b
# from sample_big_pkg.subpkg1.module1b import spam
# from sample_big_pkg.subpkg2.module2a import eggs
# from sample_big_pkg import module0

# relative import
from . import module1b
from .module1b import spam
from ..subpkg2.module2a import eggs
from .. import module0


def show():
    spam()
    eggs()
    print('show 1a')


if __name__ == "__main__":
    print('main 1a')
