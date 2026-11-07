from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def main():

    spark = SparkSession.builder \
        .appName("Customer_ETL") \
        .getOrCreate()

    source_df = spark.read \
        .option("header", True) \
        .csv("/FileStore/input/customers.csv")

    transformed_df = source_df.filter(
        col("customer_id").isNotNull()
    )

    transformed_df.write \
        .mode("overwrite") \
        .format("delta") \
        .saveAsTable("default.customers")

if __name__ == "__main__":
    main()
