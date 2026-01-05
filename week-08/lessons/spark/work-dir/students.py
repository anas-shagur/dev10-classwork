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


# 0. Print all students
for row in df.collect():
    print(row)

# 1. Remove na (could always use a subset: first_name, last_name, email)

# 2. Remove duplicates

# 3. Change birthdate to date type

# 4. Print the first 5 rows.

# 5. Print the last 3 rows.

# 6. Print students from Argentina.

# 7. Print students whose last names starts with 'T'.

# 8. Print students from Argentina, ordered by GPA.

# 9. Print the bottom 10% (100 students) ranked by GPA.

# 10. Print the 4th - 6th ranked students by GPA from Argentina.

# 11. Is anyone from Maldives?

# 12. Print summary info by column. Does everyone have a non-null email address?

# 13. Who has the latest birthday? Who is the youngest?

# 14. Who has the highest GPA? There may be a tie.

# 15. Count students per country.

# 16. Count students per country. Order by most to fewest students.

# 17. Print every course students are registered for, including repeats.

# 18. Print a distinct list of courses students are registered for.

# 19. Print a distinct list of courses students are registered for, ordered by name.

# 20. Print students who are currently registered for 5 courses.

# 21. Print students who are registered for the course "Literary Genres".

# 22. Count registrations per course.

# 23. How many registrations are not graded (grade_type is 'AUDIT')?

# 24. Create a new named tuple with fields for country, major, and iq.
# Map students to that named tuple, then sort and limit by IQ (your choice of low or high).

# Spark DataFrames do NOT support namedtuples. We cannot include Python objects.


# 25. Print the average GPA for each country. (fake data)

# 26. What is the maximum GPA per country? (fake data)

# 27. Print average IQ per Major ordered by IQ ascending.(fake data)

# 28. Who has the highest pointPercent in "Sacred Writing"?

spark.stop()
