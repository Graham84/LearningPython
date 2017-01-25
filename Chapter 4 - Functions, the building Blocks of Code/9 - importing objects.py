# karma/test_nt.py
import unittest                     # imports the unittest module
from math import sqrt               # imports one function from math
from random import randint, sample  # two imports at once
from mock import patch
from nose.tools import (            # multiline import
    assert_equal,
    assert_list_equal,
    assert_not_in,
)
from karma import nt, utils
