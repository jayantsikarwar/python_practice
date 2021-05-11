import sys

def write_df(difficulty_df,output_file,output_header,spark) :
    try:
        if output_header==difficulty_df.columns:
           print('correct Header')
           difficulty_df.write.format('csv').option('header',True).mode('overwrite').option('sep',',').save(output_file)
        else:
           print('incorrect Header')
           sys.exit(1)
        return("CSV Written Successful")
    except Exception as e:
        print("Error on file writing",e.__class__,"occured")
        sys.exit(1)