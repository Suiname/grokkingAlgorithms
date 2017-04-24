""" Binary Search in Python """
def binary_search(sorted_list, item):
    """ Binary Search function """
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) / 2
        guess = sorted_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print binary_search(my_list, 3)
print binary_search(my_list, -1)