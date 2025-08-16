from pyspark import SparkConf,SparkContext
import os 
os.environ['PYSPARK_PYTHON'] ="C:/anaconda3/envs/py310/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf =conf)

rdd = sc.parallelize([1,1,3,3, 5,5,7,8,8,9,10])
rdd2 = rdd.distinct()

print(rdd2.collect())