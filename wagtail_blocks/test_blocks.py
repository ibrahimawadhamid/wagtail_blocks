import pytest
from .blocks import *


def test_import_wagtail():
    with pytest.raises(NameError):
        blocks
