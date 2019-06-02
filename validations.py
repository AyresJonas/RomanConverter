def is_invalid_number(number):
  return not isinstance(number, int) or number < 0 or number > 3999
