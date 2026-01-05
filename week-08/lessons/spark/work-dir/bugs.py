from pyspark.sql import SparkSession
from pyspark.sql.functions import udf

spark = SparkSession.builder.getOrCreate()

bugs_df = spark.createDataFrame(
    [(10, 8), (3, 1), (7, 8), (5, 5), (9, 6)],
    schema=["bugs", "fungi"],
)

bugs_df.show()

# no index because it would be inefficient
bugs_df.select("bugs").show()
print(type(bugs_df.select("bugs")))
bugs_df.select("fungi").show()
print(bugs_df.columns)

bugs_df.printSchema()
bugs_df.describe().show()

print("first two rows")
print(bugs_df.head(2))
print("first two rows")
print(bugs_df.take(2))
print("last two rows")
print(bugs_df.tail(2))

bugs_df.groupBy().sum().show()

forager_dict = {
    10: "Jeordie",
    3: "Samantha",
    7: "Mr Pickles",
    5: "Rose",
    9: "Guy",
}

map_forager = udf(lambda x: forager_dict.get(x, None))
bugs_df = bugs_df.withColumn("forager", map_forager(bugs_df["bugs"]))

bugs_df.show()

print(type(bugs_df))
print(type(bugs_df.select("bugs")))
print(type(bugs_df["bugs"]))
print(type(bugs_df.select("bugs", "fungi")))

# rows
print(bugs_df.count())
bugs_df.filter(bugs_df["bugs"] > 5).show()
print(bugs_df.filter(bugs_df["bugs"] == 10).collect()[0])
print(bugs_df.filter(bugs_df["bugs"] == 100).collect())

spark.stop()
