from pyspark import SparkConf,SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:\\anaconda3\\envs\\py310\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([('man',99),('man',88),('women',99),('women',66)])
rdd2 = rdd.reduceByKey(lambda a,b:a+b)

print(rdd2.collect())
