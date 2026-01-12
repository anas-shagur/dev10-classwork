# (film_title: string, genre: string)

films = [
    ("Let the Right One In", "Horror"),
    ("Lady and the Tramp", "Kids"),
    ("The Aristocrats", "Comedy"),
    ("Evil Dead 2", "Horror"),
]

# 1. Use dictionary comprehension to create a dictionary of films
# where the key is the title of the film and the value is the film tuple.
# 2. Print the dictionary to the console.

dict = {
    title: (title, genre)
    for title, genre in films
}

print(dict)