
import pytest
from simple_function import add_two_numbers, mult_two_numbers, calc_two_numbers

'''
run from command line:
> python -m pytest
'''

@pytest.mark.parametrize('expected_results',
                         [(add_two_numbers, 2, 3, 5),
                          (mult_two_numbers, 4, 5, 20)],
                         ids=['add_scenario', 'mult_scenario'])
def test_add_and_mult(expected_results):

    func, arg1, arg2, expected_result = expected_results

    assert calc_two_numbers(func, arg1, arg2) == expected_result



