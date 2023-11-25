stuff = {'rope': 1, 'torch': 6, 'Gold Chain': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['torch', 'Gold Chain', 'arrow', 'ruby']

def displayInventory(inventory):
    item_count = 0
    for k, v in inventory.items():
            item_count += v
    return item_count

def addToInventory(inventory, dragonLoot):
    for loot in dragonLoot:
        inventory[loot] = inventory.get(loot, 0) + 1

addToInventory(stuff, dragonLoot)

print('Items in your inventory:')
print('- Rope           : ' + str(stuff.get('rope', 0)))
print('- Torch          : ' + str(stuff.get('torch', 0)))
print('- Gold Chain     : ' + str(stuff.get('Gold Chain', 0)))
print('- Dagger         : ' + str(stuff.get('dagger', 0)))
print('- Arrow          : ' + str(stuff.get('arrow', 0)))

print('Total items in your inventory:', displayInventory(stuff))