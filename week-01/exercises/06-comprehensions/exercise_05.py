# (film_title: string, genre: string)
films = [
    ("IT", "Horror"),
    ("The Lion King", "Kids"),
    ("The Dark Knight", "Action"),
    ("The Godfather", "Drama"),
    ("The Shawshank Redemption", "Drama"),
    ("The Avengers", "Action"),
    ("The Incredibles", "Kids"),
    ("The Shining", "Horror"),
]

# 1. Create a list of film titles that are in the 'Drama' genre using list comprehension.
# 2. Print the list to the console.
# Expected: ['The Godfather', 'The Shawshank Redemption']

print([i[0] for i in films if i[1] == "Drama"])