from national_forests import national_forests

# National forests is a list of tuples.
# (name: str, state: str, established: datetime.date, area: int)
# Each tuple contains the name of the forest, the state it is in, the date it was established, and the area in acres.
print(national_forests)

# 1. Create a list comprehension that extracts the names of the national forests.

# 2. Create a list comprehension that extracts national forest tuples that are in California.

# 3. Create a list comprehension that extracts national forest tuples that were established before 1900.

# 4. Create a list comprehension that extracts national forest tuples that are larger than 1,000,000 acres.

# 5. Create a list comprehension that transforms a state name to its abbreviation, replacing the state name in the tuple.
# (name: str, state_name: str, established: datetime.date, area: int)
# ------------------------------------------------------------------
# (name: str, state_abbr: str, established: datetime.date, area: int)

# 6. Create a dictionary comprehension that maps the state abbreviation to the number of national forests in that state.
# You can either use https://docs.python.org/3/library/collections.html#collections.Counter
# or loop through the list of national forests and count the number of forests in each state.
