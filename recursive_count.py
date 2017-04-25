def count(arr):
  if len(arr) == 0:
    return 0
  elif len(arr) == 1:
    return 1
  else:
    return 1 + count(arr[1:])

test_array = [2,4,6]
print(count(test_array))