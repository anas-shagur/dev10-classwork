# Intermediate Tuples
from datetime import date

# (national forest name, state, established date, acres)
superior_forest = ("Superior", "Minnesota", date.fromisoformat("1909-02-13"), 2_093_590)

# (town name, state, population)
ely = ("Ely", "Minnesota", 3268)

# 1. Combine the superior_forest and ely tuples into a new tuple and print it.
# Expected: ('Superior', 'Minnesota', datetime.date(1909, 2, 13), 2093590, 'Ely', 'Minnesota', 3268)
print(superior_forest + ely)
