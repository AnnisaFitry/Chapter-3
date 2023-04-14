import sys
from operator import  add
from pyspark import SparkContext as sc

access_log = sc.textFile("file:/home/cloudera/spark-2.0.0-bin-hadoop2.7/pendidikan.txt", 4)

error_log = access_log.filter(lambda x: "tinggi" in x)

cached_log = error_log.cache()

print ("Total number of error records are %s" % (cached_log.count()))
print ("Number of product pages visited that have Errors is %s" % (cached_log.filter(lambda x: "pendidikan" in x).count()))
