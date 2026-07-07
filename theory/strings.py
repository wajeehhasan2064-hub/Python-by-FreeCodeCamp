#in operator
str1 = 'Hello World'
print('Hello' in str1)

#length operator
print(len(str1))

#index operator
print(str1[4])

#negative indexing
print(str1[-1])

#string concatenation
name = 'Wajeeh'
name1 = 'Hasan'
name2 = name + ' ' + name1
print(name2)

age = 19
name3 = name1 + str(age)
print(name3)

#string slicing
#string[start:stop:step]
a = 'World is happy'
print(a[2:8:2])

#to reverse a string
print(a[::-1])

university = 'FAST Nuces'

#upper()
print(university.upper())

#lower()
print(university.lower())

#strip()
school = '     Eighty Eight     '
school1 = school.strip()
print(school1)

#replace()
uni = university.replace('FAST', 'NUST')
print(uni)

#split()
print(university.split())

#join
z = ['wajeeh', 'hasan']
print(''.join(z))

#startswith()
print(university.startswith('FAST'))

#endswith()
print(university.endswith('Nuces'))

#find()
print(university.find('FAST'))

#count()
print(uni.count('N'))

#capitalize()
print(a.capitalize())

#isupper()
print(a.isupper())

#islower
print(a.islower())

#title()
print(a.title())

#maketrans()
#str.maketrans(x, y, z)
#x → characters to replace
#y → characters to replace them with
#z → characters to remove (optional)
x = str.maketrans('abc', '123')
y = 'a cat and a ball'
print(y.translate(x))