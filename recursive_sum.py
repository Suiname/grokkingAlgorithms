def sum(arr):
  if len(arr) == 0:
    return 0
  elif len(arr) == 1:
    return arr[0]
  else:
    return sum(arr[1:]) + arr[0]

test_array = [2,4,6]
print(sum(test_array)