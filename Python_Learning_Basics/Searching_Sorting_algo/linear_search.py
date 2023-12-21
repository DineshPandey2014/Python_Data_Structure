"""
Linear search of the element
Here the list iterate each element
"""
def linear_search(x_list : list, num : int) -> int:
  for i in x_list:
      if i == num:
          return num, list
  return -1

"""
Linear search returning index and the element.
"""

def linear_search_return_index_element(list_one:[], num:int)->():
    for index, element in enumerate(list_one):
        if element == num:
            return index, element



if __name__ == "__main__":
    tuple_result = (linear_search_return_index_element([1,4,5,6], 5))
    print(tuple_result[0], tuple_result[1])




