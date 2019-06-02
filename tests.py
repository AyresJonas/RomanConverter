from decimal_to_roman import decimal_to_roman
from roman_to_decimal import roman_to_decimal


def run_decimal_to_roman_tests():
  print('Decimal to roman tests:')
  tests_params = [
    (2, 'II'),
    (4, 'IV'),
    (5, 'V'),
    (9, 'IX'),
    (22, 'XXII'),
    (50, 'L'),
    (40, 'XL'),
    (39, 'XXXIX'),
    (401, 'CDI'),
    (1010, 'MX'),
    (-1, 'Invalid number'),
    (None, 'Invalid number'),
    (6234, 'Invalid number'),
    (0, '')
  ]

  _run_and_show_results(decimal_to_roman, tests_params)

def run_roman_to_decimal_tests():
  print('Roman to decimal tests:')

  tests_params = [
    ('XX', 20),
    ('MMXIX', 2019),
    ('L', 50),
    ('DMXI', 'Invalid roman number'),
    ('VV', 'Invalid roman number'),
    ('XXXX', 'Invalid roman number'),
    ('MMMM', 'Invalid roman number'),
    ('XXXIX', 39),
    ('IV', 4),
    ('IX', 9),
    ('XL', 40),
    ('XC', 90),
    ('CD', 400),
    ('CM', 900),
    ('P', 'Invalid roman character')
  ]

  _run_and_show_results(roman_to_decimal, tests_params)

def _run_and_show_results(method, tests_params):
  for param, expected_result in tests_params:
    result = method(param)
    assert result == expected_result, 'Returned {}, should be {}'.format(result, expected_result)
    print('* {} -> {}'.format(param, expected_result))

def run_tests():
  run_decimal_to_roman_tests()
  run_roman_to_decimal_tests()

  print('\nAll tests passed!')

if __name__ == '__main__':
  run_tests()
