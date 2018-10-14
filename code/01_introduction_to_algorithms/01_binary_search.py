def binary_search(list, item):
  # low and high keep track of which part of the list you'll search in.
  low = 0
  high = len(list) - 1

  # While you haven't narrowed it down to one element ...
  while low <= high:
    # ... check the middle element
    mid = (low + high) // 2
    guess = list[mid]
    # Found the item.
    if guess == item:
      return mid
    # The guess was too high.
    if guess > item:
      high = mid - 1
    # The guess was too low.
    else:
      low = mid + 1

  # Item doesn't exist
  return None

my_list = [1, 3, 5, 7, 9]
print binary_search(my_list, 3) # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print binary_search(my_list, -1) # => None

# Can you implement this in the programming languages you know try Scala and R

# What are the applications of binary search?
# fast lookup of a dictionary/list
# Making games such as guess the number
# I can use a variant of it to search for a bases or motifs
