# test_example_functions.py
import pytest
from example_functions import my_adder, my_thermo_stat, have_digits


def test_my_adder():
    assert my_adder(2, 3, 4) == 9


def test_thermor_stat():
    assert my_thermo_stat(5, 10) == "off"


def test_have_digits():
    assert have_digits("ismail23") == 1
