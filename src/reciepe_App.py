import pyspark
from pyspark.sql import SparkSession
import os
import sys
from pyspark.sql.types import IntegerType
from read_Reciepes import read_Reciepes
from transform_Reciepes import transform_Reciepes
from write_df import write_df
from time_conv import time_conv
import configparser

if __name__ == '__main__' :
    file_name=sys.argv[1]
    output_file=sys.argv[2]
    spark = SparkSession.builder.appName("Reciepes_Kafka").getOrCreate()
    ##Read-Config-File#####
    config=configparser.RawConfigParser()
    config.read('config.ini')
    input_header= config.get('Reciepe','input_header').encode('ascii','ignore')
    input_header=input_header.split(',')
    read_file_format=config.get('Reciepe','file_format').encode('ascii','ignore')
    final_sql=config.get('Reciepe','final_sql').encode('ascii','ignore')
    output_header= config.get('Reciepe','output_header').encode('ascii','ignore')
    output_header=outut_header.split(',')
    read=read_Reciepes(file_name,read_file_format,input_header,spark)
    spark.udf.register("time_conv",time_conv,IntegerType())
    transform=transform_Reciepes(read,final_sql,spark)
    write=write_df(transform,output_file,output_header,spark)
    print(write)