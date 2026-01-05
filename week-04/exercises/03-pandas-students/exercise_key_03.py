import ast
from collections import namedtuple
from datetime import datetime

import pandas as pd

df = pd.read_csv("students.csv")
# Do not change.
# This ensures registrations are converted from string to list.
df["registrations"] = df["registrations"].apply(ast.literal_eval)
# print(df.info())

# 0. Print all students
for label, content in df.iterrows():
    print(content)

# 1. Remove na (could always use a subset: first_name, last_name, email)
print(f"Original length: {len(df)}")
df = df.dropna()
print(f"Drop na length: {len(df)}")

# 2. Remove duplicates
df = df.drop_duplicates(subset=["first_name", "last_name", "email"], keep="first")
print(f"Remove duplicates length: {len(df)}")

# 3. Change birthdate to datetime64[ns]
df["birth_date"] = (
    df["birth_date"]
    .apply(lambda dt: datetime.strptime(dt, "%m/%d/%Y").date())
    .astype("datetime64[ns]")
)

# 4. Print the first 5 rows.
print(df.head())

# 5. Print the last 3 rows.
print(df.tail(3))

# 6. Print students from Argentina.
from_argentina = df[df["country"] == "Argentina"]
print(from_argentina)

# 7. Print students whose last names starts with 'T'.
last_name_starts_with_t = df[df["last_name"].str.startswith("T")]
print(last_name_starts_with_t)

# 8. Print students from Argentina, ordered by GPA.
from_argentina_sorted = from_argentina.sort_values(by="gpa", ascending=False)
print(from_argentina_sorted)

# 9. Print the bottom 10% (100 students) ranked by GPA.
bottom_10 = df.nsmallest(n=100, columns="gpa")
bottom_10_sorted = bottom_10.sort_values(by="gpa")
print(bottom_10_sorted[["email", "gpa"]])

# 10. Print the 4th - 6th ranked students by GPA from Argentina.
from_argentina_sorted = from_argentina.sort_values(by="gpa", ascending=False)
print(from_argentina_sorted[3:6])

# 11. Is anyone from Maldives?
from_maldives = df[df["country"] == "Maldives"]
print(not from_maldives.empty)

# 12. Print summary info by column. Does everyone have a non-null email address?
print(df.info())
print(df["email"].isnull().values.any())

# 13. Who has the latest birthday? Who is the youngest?
latest_birthday = df[df["birth_date"] == df["birth_date"].max()]
print(latest_birthday[["first_name", "last_name", "birth_date"]])

# 14. Who has the highest GPA? There may be a tie.
highest_gpa = df[df["gpa"] == df["gpa"].max()]
print(highest_gpa[["first_name", "last_name", "gpa"]])

# 15. Count students per country.
print(df["country"].value_counts())

# 16. Count students per country. Order by most to fewest students.
print(df["country"].value_counts().sort_values(ascending=False))

# 17. Print every course students are registered for, including repeats.
registrations = pd.json_normalize(df["registrations"].explode())
print(registrations["course"])

# 18. Print a distinct list of courses students are registered for.
print(registrations["course"].unique())

# 19. Print a distinct list of courses students are registered for, ordered by name.
print(registrations["course"].sort_values().unique())

# 20. Print students who are currently registered for 5 courses.
df["registration_count"] = df["registrations"].apply(len)
registered_for_5 = df[df["registration_count"] == 5]
print(registered_for_5)

# 21. Print students who are registered for the course "Literary Genres".
literary_genres = df[
    df["registrations"].apply(
        lambda regs: any(r["course"] == "Literary Genres" for r in regs)
    )
]
print(literary_genres)

# 22. Count registrations per course.
registrations_per_course = registrations["course"].value_counts()
print(registrations_per_course)

# 23. How many registrations are not graded (grade_type is 'AUDIT')?
audited = registrations[registrations["grade_type"] == "AUDIT"]
print(len(audited))

# 24. Create a new named tuple with fields for country, major, and iq.
# Map students to that named tuple, then sort and limit by IQ (your choice of low or high).
Student = namedtuple("Student", ["country", "major", "iq"])
# This is a Pandas Series of named tuples
students_named_tuple = df.apply(
    lambda row: Student(country=row["country"], major=row["major"], iq=row["iq"]),
    axis=1,
)
students_named_tuple_sorted = sorted(
    students_named_tuple, key=lambda x: x.iq, reverse=True
)
print(students_named_tuple_sorted[:5])

# 25. Print the average GPA for each country. (fake data)
average_gpa_per_country = df.groupby("country")["gpa"].mean()
print(average_gpa_per_country)

# 26. What is the maximum GPA per country? (fake data)
max_gpa_per_country = df.groupby("country")["gpa"].max()
print(max_gpa_per_country)

# 27. Print average IQ per Major ordered by IQ ascending.(fake data)
average_iq_per_major = df.groupby("major")["iq"].mean().sort_values()
print(average_iq_per_major)

# 28. Who has the highest pointPercent in "Sacred Writing"?
df["sacred_writing_points"] = df["registrations"].apply(
    lambda regs: next(
        (r["point_percent"] for r in regs if r["course"] == "Sacred Writing"), None
    )
)
highest_sacred_writing_points = df[
    df["sacred_writing_points"] == df["sacred_writing_points"].max()
]
print(highest_sacred_writing_points)
