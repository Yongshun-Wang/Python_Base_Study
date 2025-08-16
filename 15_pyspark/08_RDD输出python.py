from pyspark import SparkConf,SparkContext
import os 
os.environ['PYSPARK_PYTHON'] ="C:/anaconda3/envs/py310/python.exe"
os.environ['PYSPARK_HADOOP'] = "C:\\hadoop"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism","1")

sc = SparkContext(conf =conf)

rdd = sc.parallelize([1,2,3,4,5])

# rdd_list:list = rdd.collect()
# print(rdd_list)
# print(type(rdd_list))

# print(rdd.reduce(lambda a,b:a+b))

# print(rdd.take(3))

# print(rdd.count())

rdd.saveAsTextFile("output")