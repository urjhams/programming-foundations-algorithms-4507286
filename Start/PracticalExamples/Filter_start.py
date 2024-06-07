# Example file for Programming Foundations: Algorithms by Joe Marini
# use a set to count unique items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a set to perform a filter
unique_items = set(items)

# TODO: loop over each item and add to the set
print(unique_items)

# TODO: Count the unique letters in a sentence
sentence = "The quick brown fox jumps over the lazy dog."

uniques = set()
for char in sentence.lower():
  if char.isalnum(): uniques.add(char)
print(uniques)
