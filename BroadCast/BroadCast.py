from pyspark import SparkContext as sc
broadcastVar = sc.broadcast(list(range(1, 100)))
broadcastVar.value 	