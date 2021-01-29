def list_even(num_list):

  even_numbers = []

  for num in num_list:
    if num % 2 == 0:
      even_numbers.append(num)
    else:
      pass

  return even_numbers


list_even([2,4,6,5,7])
