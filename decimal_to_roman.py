import sys
from validations import is_invalid_number


_DECIMAL_TO_ROMAN_DICT = {
  1000: 'M',
  900: 'CM',
  500: 'D',
  400: 'CD',
  100: 'C',
  90: 'XC',
  50: 'L',
  40: 'XL',
  10: 'X',
  9: 'IX',
  5: 'V',
  4: 'IV',
  1: 'I'
}

def decimal_to_roman(number):
  if is_invalid_number(number):
    return 'Invalid number'

  return _calculate_result(number)

def _calculate_result(number):
  roman_number = ''
  for key, value in _DECIMAL_TO_ROMAN_DICT.items():
    while number >= key:
      number -= key
      roman_number += value

  return roman_number

if __name__ == '__main__':
  number = int(sys.argv[1])
  print(decimal_to_roman(number))
