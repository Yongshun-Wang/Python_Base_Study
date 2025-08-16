# 代码本身没有语法错误，但存在以下问题：
# 1. 路径问题：sc.textFile("../15_pyspark/search_log.txt")，如果当前工作目录不是该文件的上级目录，会找不到文件，建议使用绝对路径或确保工作目录正确。
# 2. PYSPARK_HADOOP 环境变量名写错了，应该是 'HADOOP_HOME'，否则不会生效。
# 3. 业务逻辑：x.split("\t")[0][:2] 取的是时间字段的前两位（如 '00'），如果需求是统计每个小时的访问量，这样没问题，但如果需求不是按小时统计，则需调整。
# 4. 资源释放：sc 用完后建议 sc.stop() 释放资源。
# 5. 代码风格：建议加上 main 保护。

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:/anaconda3/envs/py310/python.exe"
os.environ['HADOOP_HOME'] = "C:\\hadoop"  # 正确的环境变量名

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism","1")
sc = SparkContext(conf=conf)

file_path = sc.textFile("E:\\Python_base_study\\15_pyspark\\search_log.txt")  # 路径需确保正确


#1.热门搜索时间段
# result1 = file_path.map(lambda x: (x.split("\t")[0][:2], 1)) \
#     .reduceByKey(lambda a, b: a + b) \
#     .sortBy(lambda x: x[1], ascending=False, numPartitions=1) \
#     .take(3)
# print("需求1的结果:", result1)

#2.热门搜索词
# result2 = file_path.map(lambda x: (x.split("\t")[2], 1)) \
#     .reduceByKey(lambda a, b: a + b) \
#     .sortBy(lambda x: x[1], ascending=False, numPartitions=1) \
#     .take(3)
# print("需求2的结果:", result2)

#3.黑马程序员被搜索的最多时段
result3 = file_path.map(lambda x: (x.split("\t"))) \
    .filter(lambda x:x[2]=='黑马程序员')\
    .map(lambda x:(x[0][:2],1))\
    .reduceByKey(lambda a, b: a + b) \
    .sortBy(lambda x: x[1], ascending=False, numPartitions=1) \
    .take(1)
print("需求3的结果:", result3)

#4.转换为JSON格式存储
file_path.map(lambda x:x.split("\t"))\
    .map(lambda x:{"time":x[0],"user_id":x[1],"key_word":x[2],"rank1":x[3],"rank2":x[4],"url":x[5]})\
    .saveAsTextFile("output_json")

sc.stop()  # 释放资源
