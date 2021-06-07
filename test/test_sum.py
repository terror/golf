import pytest, sys
from src import sum_even, sum_odd

@pytest.fixture
def odd():
  return {
    4: [1, 2, 3],
    4: [2, 4, 6, 8, 1, 1, 1, 1],
    401: [100, 200, 300, 401],
    1048: [1047, 1, 20, 48]
  }

@pytest.fixture
def even():
  return {
    2: [1, 2, 3],
    20: [2, 4, 6, 8, 1, 1, 1, 1],
    600: [100, 200, 300, 401],
    68: [1047, 1, 20, 48]
  }

def test_sum_even(even):
  for k, v in even.items():
    assert sum_even(v) == k

def test_sum_odd(odd):
  for k, v in odd.items():
    assert sum_odd(v) == k
