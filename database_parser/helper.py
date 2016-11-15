"""
File containing all the helper functions
"""

# Checks if all the elements of array are present
# as keys in the given dictioning
def check_array_elems_as_dict_keys(array, dictionary):
  if len(set(array).difference(dictionary.keys())) == 0:
    return True
  return False

# Checks the validity of the arguments supplied
# in terms of ensuring that the required arguments 
# are supplied by the user
def check_argument_validity(required_args, arg_dict):
  if not check_array_elems_as_dict_keys(required_args, arg_dict):
    raise Exception('All the required arguments: ' + str(required_args) + ' not supplied.')

if __name__ == '__main__':
  print(check_array_elems_as_dict_keys(['1', '2'], {'1':'a', '2':'b'}))
  print(check_array_elems_as_dict_keys(['1', '3'], {'1':'a', '2':'b'}))

# If only the first column of the query result is 
# required, then this helper is used to parse the 
# data and render a tuple containing only the first column
def parse_query_data(data):
  return tuple(map(lambda x: x[0], data))
