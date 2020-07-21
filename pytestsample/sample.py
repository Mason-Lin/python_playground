import tempfile
from pytestsample.module import module
from pathlib import Path

import pytest


def test_add():
    win_temp = tempfile.gettempdir()
    print(type(win_temp))
    

if __name__ == "__main__":
    pytest.main()

