print('''Try:
    - py test_pkg.py
    - pipenv run python test_pkg.py
''')

try:
    import requests
except ImportError:
    raise
else:
    print(requests.__version__)

try:
    import numpy
except ImportError:
    raise
else:
    print(numpy.__version__)
