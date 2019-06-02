def _is_invalid_combination(first, second):
  valid_combinations = [
    (1, 5),
    (1, 10),
    (10, 50),
    (10, 100),
    (100, 500),
    (100, 1000)
  ]

  return not valid_combinations.__contains__((first, second))

def _is_repeated_twice(first_num, second_num):
  return first_num == second_num and (first_num == 5 or first_num == 50 or first_num == 500)

def _is_repeated_more_than_four_times(number_list):
  idx_lists = { 1: [], 10: [], 100: [] }
  for idx in range(0, len(number_list)):
    if number_list[idx] == 1 or number_list[idx] == 10 or number_list[idx] == 100:
      idx_lists[number_list[idx]].append(idx)

  for value in idx_lists.values():
    if _is_length_greater_than_three(value) and _is_consecutive(value):
      return True

def _is_length_greater_than_three(_list):
  return len(_list) > 3

def _is_consecutive(_list):
  return _list[0] + 1 == _list[1] and _list[1] + 1 == _list[2] and _list[2] + 1 == _list[3]

def is_invalid_roman_number(number_list):
  if _is_repeated_more_than_four_times(number_list):
    return True
  for first_num, second_num in zip(number_list, number_list[1:]):
    if _is_repeated_twice(first_num, second_num):
      return True
    if second_num > first_num and _is_invalid_combination(first_num, second_num):
      return True

  return False

def is_invalid_number(number):
  return not isinstance(number, int) or number < 0 or number > 3999
