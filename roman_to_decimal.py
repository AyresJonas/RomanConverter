import sys
from validations import is_invalid_roman_number


_ROMAN_TO_DECIMAL_DICT = {
  'M': 1000,
  'D': 500,
  'C': 100,
  'L': 50,
  'X': 10,
  'V': 5,
  'I': 1
}

def roman_to_decimal(roman_number):
  try:
    if len(roman_number) == 1:
      return _ROMAN_TO_DECIMAL_DICT[roman_number]

    decimals = [_ROMAN_TO_DECIMAL_DICT[char] for char in roman_number]
  except KeyError:
    return 'Invalid roman character'

  if is_invalid_roman_number(decimals):
    return 'Invalid roman number'

  result = _calculate_result(decimals)
  if result > 3999:
    return 'Invalid roman number'

  return result

def _calculate_result(decimals):
  result = 0
  for first_num, second_num in zip(decimals, decimals[1:]):
    if first_num >= second_num:
      result += first_num
    else:
      result -= first_num

  return result + second_num

if __name__ == '__main__':
  roman_num = sys.argv[1].upper()
  print(roman_to_decimal(roman_num))
