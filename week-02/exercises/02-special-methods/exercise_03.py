import copy
# from spotify_extractor import find_all_tracks


# 1. In our `Track` class, override __str__ for a human readable string representation.
# Override __repr__ for a developer-focused string representation.

# 2. Print tracks from find_all_tracks() using the __str__ method.

# 3. Override __eq__ to compare two tracks based on their id attribute.

# 4. Take the first item in the list and use `copy.deepcopy` to create a new track object.
# Compare the original track with the copied track using the `==` operator.
# Expected output: True

# track_copy = copy.deepcopy(tracks[0])

# 5. Compare the first and second tracks in the list using the `==` operator.
# Expected output: False

# 6. The __lt__ method is used to sort objects. Override __lt__ to compare track names alphabetically.

# 7. Sort the tracks list using the `sort` method. This sorts in-place.

# 8. Print the first 25 tracks in the list.


# 9. We can also order by multiple attributes. With __lt__, there are two options:
# Option 1: If the track names are the same, sort by artist.
# def __lt__(self, other):
#     # Secondary comparison: artist
#     if self.track == other.track:
#         return self.artist < other.artist
#     # Primary comparison: track
#     return self.track < other.track
# =====================================
# Option 2: Compare tuples.
# def __lt__(self, other):
#     return (self.track, self.artist) < (other.track, other.artist)

# 10. Sort tracks and print.

# 11. Use a `for` loop and the `sorted` function
# with a lambda function to sort by danceability.

# 12. Stretch goal: Use the `Counter` class to count the number of tracks per artist.
# Documentation: https://docs.python.org/3/library/collections.html#counter-objects
# Print the artist and count.
