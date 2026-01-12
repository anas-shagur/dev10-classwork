commonly_misspelled_words = [
    "indict",
    "fiery",
    "misspell",
    "comparsion",
    "perseverance",
]

for word in commonly_misspelled_words:
    print(word)

commonly_misspelled_words[3] = "comparison"

for word in commonly_misspelled_words:
    print(word)

# One of the commonly_misspelled_words is misspelled.
# 1. Change it to the correct spelling. Don't alter the list literal declaration. Set the value by index.
# (We can always use the VS Code spell-checker extension:
#  https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
# 2. Loop a second time and confirm all five words are spelled correctly.
