from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Create Spark session
spark = SparkSession.builder.appName("Customer Demographics Processing").getOrCreate()

# Load the dataset
df = spark.read.csv("data/retailstore_large.csv", header=True, inferSchema=True)

# Preview schema and data
df.printSchema()
df.show(5)

# Drop rows with missing values
df = df.dropna()

# View average salary by gender
df.groupBy("Gender").agg(avg("Salary").alias("Avg_Salary")).show()

# View average salary by country
df.groupBy("Country").agg(avg("Salary").alias("Avg_Salary")).show()

# Export cleaned data for ML use
df.toPandas().to_csv("retail_cleaned.csv", index=False)
