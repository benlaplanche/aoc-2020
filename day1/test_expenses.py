# test_expenses.py

import pytest
from expenses import *


def test_expenses():
    expense_list = [1721, 979, 366, 299, 675, 1456]
    assert calculate_total(expense_list) == 514579
