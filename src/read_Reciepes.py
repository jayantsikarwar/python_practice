import sys

def read_Reciepes(file_name,read_file_format,input_header,spark) :
    try:
        reciepes_df=spark.read.format(read_file_format).option('InferSchema','True').option('header','True').load(file_name)
        cols=reciepes_df.columns
        if cols == input_header :
           return reciepes_df
        else :
           print("invailid_header",cols)
           sys.exit(1)
    except Exception as e:
        print("read error",e.__class__,"occured")
        sys.exit(1)