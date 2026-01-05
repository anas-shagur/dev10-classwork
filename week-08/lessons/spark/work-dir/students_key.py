from collections import namedtuple

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    explode,
    expr,
    from_json,
    max,
    size,
    to_date,
)

from pyspark.sql.types import (
    ArrayType,
    StructType,
    StructField,
    StringType,
    IntegerType,
)


spark = SparkSession.builder.getOrCreate()

df = spark.read.csv("students.csv", header=True, inferSchema=True)

# Do not change.
# This ensures registrations are converted from string to an array of structs.
registration_schema = ArrayType(
    StructType(
        [
            StructField("grade_type", StringType(), True),
            StructField("point_percent", IntegerType(), True),
            StructField("course", StringType(), True),
        ]
    )
)

# Parse the 'registrations' column (JSON-style string) into real Array[Struct]
df = df.withColumn(
    "registrations", from_json(col("registrations"), registration_schema)
)

df.select("first_name", "registrations").show()


# 0. Print all students
for row in df.collect():
    print(row)

# 1. Remove na (could always use a subset: first_name, last_name, email)
print(f"Original length: {df.count()}")
df = df.filter(
    col("first_name").isNotNull()
    & col("last_name").isNotNull()
    & col("email").isNotNull()
)
print(f"Drop na length: {df.count()}")

# 2. Remove duplicates
df = df.dropDuplicates()
print(f"Remove duplicates length: {df.count()}")

# 3. Change birthdate to date type
df = df.withColumn("birth_date", to_date(col("birth_date"), "M/d/yyyy"))
df.show()

# 4. Print the first 5 rows.
print(df.head(5))

# 5. Print the last 3 rows.
print(df.tail(3))

# 6. Print students from Argentina.
from_argentina_df = df.filter(df["country"] == "Argentina")
from_argentina_df.show()

# 7. Print students whose last names starts with 'T'.
last_name_starts_with_t_df = df.filter(df["last_name"].startswith("T"))
last_name_starts_with_t_df.show()

# 8. Print students from Argentina, ordered by GPA.
from_argentina_sorted_gpa_df = from_argentina_df.orderBy("gpa")
from_argentina_sorted_gpa_df.show()

# 9. Print the bottom 10% (100 students) ranked by GPA.
df.orderBy("gpa").limit(100).show()

# 10. Print the 4th - 6th ranked students by GPA from Argentina.
print(from_argentina_sorted_gpa_df.take(6)[3:6])

# 11. Is anyone from Maldives?
from_maldives_df = df.filter(df["country"] == "Maldives")
from_maldives_df.show()


# 12. Print summary info by column. Does everyone have a non-null email address?
df.printSchema()
print(f"NA email count: {df.filter(df['email'].isNull()).count()}")

# 13. Who has the latest birthday? Who is the youngest?
latest_birthday = df.select(max("birth_date")).collect()[0][0]
latest_birthday_df = df.filter(df["birth_date"] == latest_birthday)
latest_birthday_df.select("first_name", "last_name", "birth_date").show()

# 14. Who has the highest GPA? There may be a tie.
highest_gpa = df.select(max("gpa")).collect()[0][0]
df.filter(df["gpa"] == highest_gpa).show()

# 15. Count students per country.
df.groupBy("country").count().show()

# 16. Count students per country. Order by most to fewest students.
df.groupBy("country").count().orderBy("count", ascending=False).show()

# 17. Print every course students are registered for, including repeats.
registrations_df = df.select(explode("registrations").alias("registrations"))
registrations_df.show()

# 18. Print a distinct list of courses students are registered for.
registrations_df.select("registrations.course").distinct().show()

# 19. Print a distinct list of courses students are registered for, ordered by name.
registrations_df.select("registrations.course").distinct().orderBy("course").show()

# 20. Print students who are currently registered for 5 courses.
df = df.withColumn("registration_count", size("registrations"))
registered_for_5_df = df.filter(df["registration_count"] == 5)
registered_for_5_df.show()


# 21. Print students who are registered for the course "Literary Genres".
lit_genres_df = df.filter(
    expr("exists(registrations, x -> x.course = 'Literary Genres')")
)
lit_genres_df.show(truncate=False)

# 22. Count registrations per course.
registrations_per_course_df = registrations_df.groupBy("registrations.course").count()
registrations_per_course_df.show()


# 23. How many registrations are not graded (grade_type is 'AUDIT')?
audited_df = registrations_df.filter(
    registrations_df["registrations.grade_type"] == "AUDIT"
)
print(f"AUDIT grades: {audited_df.count()}")


# 24. Create a new named tuple with fields for country, major, and iq.
# Map students to that named tuple, then sort and limit by IQ (your choice of low or high).
Student = namedtuple("Student", ["country", "major", "iq"])

# Spark DataFrames do NOT support namedtuples. We cannot include Python objects.

# Select columns and sort.
students_df = df.select("country", "major", "iq").orderBy(col("iq").desc())

# Convert to named tuples.
students_named_tuples = [
    Student(row["country"], row["major"], row["iq"]) for row in students_df.collect()
]

# Limit
top_5 = students_named_tuples[:5]
for student in top_5:
    print(student)


# 25. Print the average GPA for each country. (fake data)
average_gpa_per_country_df = df.groupBy("country").avg("gpa")
average_gpa_per_country_df.show()

# 26. What is the maximum GPA per country? (fake data)
max_gpa_per_country_df = (
    df.groupBy("country").max("gpa").orderBy("max(gpa)", ascending=False)
)
max_gpa_per_country = max_gpa_per_country_df.collect()[0][1]
max_gpa_per_country_df.filter(
    max_gpa_per_country_df["max(gpa)"] == max_gpa_per_country
).show()


# 27. Print average IQ per Major ordered by IQ ascending.(fake data)
avg_iq_per_major_df = df.groupBy("major").avg("iq").orderBy("avg(iq)")
avg_iq_per_major_df.show()

# 28. Who has the highest pointPercent in "Sacred Writing"?
max_sacred_writing_pts = (
    registrations_df.filter(
        registrations_df["registrations.course"] == "Sacred Writing"
    )
    .select(max("registrations.point_percent"))
    .collect()[0][0]
)

sacred_writing_most_points_df = df.filter(
    expr(
        f"exists(registrations, x -> x.course = 'Sacred Writing' and x.point_percent = {max_sacred_writing_pts})"
    )
)

sacred_writing_most_points_df.show()

spark.stop()
