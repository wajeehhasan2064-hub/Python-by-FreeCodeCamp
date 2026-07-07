#input() -> to take the input from the user

#we use def() when we have to make our own function
def wajeeh():
    print('wajeeh')

wajeeh()

#local scope -> function declared inside a class can only be accessible inside the class
#global scope -> can be accessed anywhere
#built-in -> functions already built inside the python language
#enclosing scope -> nested function inside a function can access the variable of the function

#LISTS and TUPLES

cities = ['Karachi', 'Islamabad', 'Lahore']
print(cities)
name = 'wajeeh'
print(list(name))
del cities[1]
print(cities)

#append() -> can append a new string
cities.append('Tokyo')
print(cities)

#extend() -> same thing

#insert -> can insert at specific index
cities.insert(1, 'Delhi')
print(cities)

#pop() -> to remove a specific element
cities.pop(1)
print(cities)

#clear()
cities.clear()
print(cities)

#reverse()
cities.reverse()
print(cities)

#index()
print(cities.index("Karachi"))

# TUPLES 

#they are almost same as lists