from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    concat_ws,
    explode,
    length,
    lit,
    max,
    split,
    to_date,
    upper,
)

spark = SparkSession.builder.getOrCreate()

mobile_df = spark.read.csv("mobile_devices.csv", header=True, inferSchema=True)
mobile_df.show()

# rough equivalent of pandas.info()
mobile_df.printSchema()


# head and take are equivalent
print("first 2 rows")
print(mobile_df.head(2))
print("first 2 rows")
print(mobile_df.take(2))

print("last 2 rows")
print(mobile_df.tail(2))

mobile_df.describe().show()
mobile_df.select("brand").describe().show()

newer_df = mobile_df.filter(mobile_df.release_date == 2020)
newer_df.show()

newer_df = mobile_df.filter(
    (mobile_df.release_date == 2020) | (mobile_df.release_date == 2017)
)
newer_df.show()

newer_df = mobile_df.filter(mobile_df.release_date.isin([2020, 2017]))
newer_df.show()

max_release_date = mobile_df.select(max("release_date")).collect()[0][0]
max_df = mobile_df.filter(mobile_df.release_date == max_release_date)
max_df.show()

# pandas equivalent of nsmallest
mobile_df.orderBy("release_date").limit(10).show()

original_count = mobile_df.count()  # 100
missing_os_df = mobile_df.filter(mobile_df.os.isNull())
missing_os_df.show()
missing_os_count = missing_os_df.count()  # 2

# any
print(f"any: {original_count - missing_os_count > 0}")
# all
print(f"all: {original_count == missing_os_count}")

# sort and orderBy are aliases
mobile_df.sort("brand").show()
mobile_df.sort("release_date", ascending=False).show()

# brand/phone data
data = [
    ("Samsung", ["Galaxy S21", "Galaxy Note 20", "Galaxy Z Fold 2"]),
    ("Apple", ["iPhone 12", "iPhone 12 Pro", "iPhone 12 Pro Max"]),
    ("Google", ["Pixel 5", "Pixel 4a", "Pixel 4a 5G"]),
]

brand_phone_df = spark.createDataFrame(data, ["brand", "models"])
exploded_df = brand_phone_df.select("brand", explode("models").alias("model"))
exploded_df.show()

# length
mobile_df = mobile_df.withColumn("brand_length", length("brand"))
mobile_df.show()

# model to brand
mobile_df = mobile_df.withColumn("model_abbr", split(col("model"), " ").getItem(0))
mobile_df.show()

mobile_df.printSchema()
# convert to float
mobile_df = mobile_df.withColumn("brand_length", col("brand_length").cast("float"))

# Step 1: Cast the year to string and concatenate '-01-01'
mobile_df = mobile_df.withColumn(
    "release_date",
    concat_ws("-", col("release_date").cast("string"), lit("01"), lit("01")),
)

# Step 2: Convert to actual Spark date type
mobile_df = mobile_df.withColumn("release_date", to_date("release_date", "yyyy-MM-dd"))
mobile_df.show()
mobile_df.printSchema()

# upper
mobile_df = mobile_df.withColumn("os", upper(col("os")))

mobile_df.select("os").show(5, truncate=False)

spark.stop()
