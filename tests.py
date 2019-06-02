from decimal_to_roman import decimal_to_roman


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

def _run_and_show_results(method, tests_params):
  for param, expected_result in tests_params:
    result = method(param)
    assert result == expected_result, 'Returned {}, should be {}'.format(result, expected_result)
    print('* {} -> {}'.format(param, expected_result))

def run_tests():
  run_decimal_to_roman_tests()

  print('\nAll tests passed!')

if __name__ == '__main__':
  run_tests()
