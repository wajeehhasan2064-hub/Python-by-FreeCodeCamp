# general syntax of dictionary
dictionary = {
    'key1': 'value1',
    'key2': 'value2'
}

# we can also use
pizza = dict([('name', 'wajeeh'), ('age', 19)])
print(pizza['name'])

wajeeh = {
    'name' : 'wj',
    'age' : 19, 
    'fav' : 'fries'
}

print(wajeeh.keys()) # .keys()
print(wajeeh.values()) # .values()
print(wajeeh.get('name', [])) #.get()
print(wajeeh.items()) # .items()
print(wajeeh.clear()) # .clear()
print(wajeeh.pop('age', 20)) # .pop()
print(wajeeh.update({'name':'wajeeeeeeh', 'age':25})) # .update()

# Common methods to use dictionaries

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

#to get all values
for price in products.values():
    print(price)

#to get all keys
for product in products.keys():
    print(product)

# to apply 20# discount on all items
for product, price in products.items():
    products[product] = round(price * 0.8)
print(products)

for product in enumerate(products):
    print(product)

# to get everything at a go
for index, product in enumerate(products.items()):
    print(index, product)