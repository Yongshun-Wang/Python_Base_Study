from pyspark import SparkConf,SparkContext
import os 
os.environ['PYSPARK_PYTHON'] ="C:/anaconda3/envs/py310/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf =conf)

rdd = sc.parallelize({('itheima',4),('python',5),('spark',9),('pysaprk',2)})
rdd2 = rdd.sortBy(lambda x: x[1],ascending=False,numPartitions=1)

print(rdd2.collect())