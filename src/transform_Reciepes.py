import sys

def transform_Reciepes(reciepes_df,final_sql,spark) :
    try:
        reciepes_df.createOrReplaceTempView("temp_reciepes")
    except Exception as e:
        print("read in_view_creation",e.__class__,"occured")
        sys.exit(1)
    try:
        beef_df=spark.sql("""select name from temp_reciepes where upper(ingredients) like '%BEEF%'""").show(10,False)
    except Exception as e:
        print("Error on Beef_df",e.__class__,"occured")
        sys.exit(1)
    
    try:
        difficulty_df=spark.sql("""{0}""".format(final_sql))
        return difficulty_df
    except Exception as e:
        print("Error on difficulty_df",e.__class__,"occured")
        sys.exit(1)