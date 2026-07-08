# Sets and how they work

str = {10, 20, 30, 40, 50}

# to define an empty set, set() is used instead of {}

# .add() method
str.add(60)
print(str)

# .remove() or .discard() method to remove a number
str.remove(40)
print(str)
# if number is not found, remove() will throw a keyError while discard() will not.

# .clear() method clears the whole set
# .issubset() and .issuperset() methods to check if string is a subset or superset of another string.

myset = {1, 2, 3, 4, 5}
yourset = {2, 3, 4, 5}

print(myset.issubset(yourset))
print(yourset.issuperset(myset))

# .isdisjoint() to check if both sets have any value in common
print(myset.isdisjoint(yourset))

# Union operator which shows all values of both sets
print(yourset | myset)

# Intersection operator returns a set with elemets common
print(yourset & myset)

# Difference operator returns element that are in first set but not in the other step
print(myset - yourset)

# Symmetric operator returns uncommon values of botb sets
print(myset ^ yourset)

# To check if a value is in the set or not
print(5 in myset)