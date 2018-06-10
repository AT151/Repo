inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
print(inventory)

inventory.update({"pocket": ["seashell","strange berry","lint"]})

print("done")

print(inventory)

print("done")

del inventory['backpack'][1]

print(inventory)

inventory['gold'] = inventory['gold'] + 50

print(inventory)