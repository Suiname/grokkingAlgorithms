
def max(arr):
  def find_max(array, largest):
    if len(array) == 0:
      return 0
    elif len(array) == 1:
      if largest < array[0]:
        return array[0]
      else:
        return largest
    else:
      if largest < array[0]:
        largest = array[0]
        return find_max(array[1:], largest)
      else:
        return find_max(array[1:], largest)
  return find_max(arr, 0)

test_array = [2,4,6]
print(max(test_array))