
import mock
import pytest
from simple_function import add_two_numbers, mult_two_numbers, calc_two_numbers


@pytest.mark.parametrize('expected_results', [(['add', 2, 3], 5), (['mult', 4, 5], 20)], ids=['add_scenario', 'mult_scenario'])
@pytest.mark.parametrize('run_func', [add_two_numbers, mult_two_numbers], ids=['add', 'mult'])
@mock.patch('simple_function.calc_two_numbers')
def test_add_and_mult(mock_calc, run_func, expected_results):

    func, arg1, arg2 = expected_results

    assert calc_two_numbers(run_func, arg1, arg2) == expected_results



