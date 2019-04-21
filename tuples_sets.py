# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple

fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
# print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length of fruits
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mangos'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Add duplicate
fruits_set.add('Apples')

# Remove from set
# fruits_set.remove('Grape')

# Clear set
# fruits_set.clear()

# Delete set
# del fruits_set

print(fruits_set)