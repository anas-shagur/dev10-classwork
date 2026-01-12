# SLICES
legendary_creatures = [
    "fairies",
    "goblins",
    "gnomes",
    "unicorns",
    "harpies",
    "solar fish",
]
extra_legendary_creatures = [
    "ogres",
    "dwarves",
    "elves",
    "dragons",
    "mermaids",
    "phoenixes",
    "doppelgangers",
    "cottage zombies",
    "dire wolves",
]

# Slicing syntax: sequence[start:end:step]

# 1. Print a slice of the first 3 legendary_creatures.
# Expected: ['fairies', 'goblins', 'gnomes']
print(legendary_creatures[:3])

# 2. Print a slice of the last 3 legendary_creatures.
# Hint: Use negative indexing.
# Expected: ['unicorns', 'harpies', 'solar fish']
print(legendary_creatures[-3:])

# 3. Print a slice of the middle 3 extra_legendary_creatures.
# Expected: ['dragons', 'mermaids', 'phoenixes']
print(extra_legendary_creatures[3:6])

# 4. Print a concatenated slice of the first 2 legendary_creatures and the last 2 extra_legendary_creatures.
# Expected: ['fairies', 'goblins', 'cottage zombies', 'dire wolves']
print(legendary_creatures[:2] + extra_legendary_creatures[-2:])

# 5. Delete "dwarves", "elves", and "dragons" from extra_legendary_creatures
# with a slice.
# Then print extra_legendary_creatures.
# Expected: ['ogres', 'mermaids', 'phoenixes', 'doppelgangers', 'cottage zombies', 'dire wolves']
del extra_legendary_creatures[1:4]
print(extra_legendary_creatures)

# 6. "Multiply" the last 2 legendary_creatures by 3 and print the result.
# Expected: ['harpies', 'solar fish', 'harpies', 'solar fish', 'harpies', 'solar fish']
print(legendary_creatures[-2:] * 3)