from pyspark.sql import SparkSession

# 1. create a synchronous session,
# not running in parallel
spark = SparkSession.builder.getOrCreate()

print("a first spark session...")

# 2. stops the session
spark.stop()