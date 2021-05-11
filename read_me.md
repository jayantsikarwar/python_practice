# Spark Application

Created spark application 'reciepe_App.py'  to process recipe files created from kafka at input location.

Included Config.ini file for to enable header checks and handle transformation changes.

Features:

1. Input Can be configured through Config file for json and csv files.

2. Header checks for Input and output files Config file.

3. Transformation Changes through Config file.

## Usage
Local

```
spark2-submit --master yarn --py-files "time_conv.py,transform_Reciepes.py,read_Reciepes.py,write_df.py" --files "config.ini" reciepe_App.py #input_path/#input_file #output_path/#output_file
```

Cluster
```
spark2-submit --master yarn --deploy-mode cluster --py-files "time_conv.py,transform_Reciepes.py,read_Reciepes.py,write_df.py" --files "config.ini" reciepe_App.py #input_path/#input_file #output_path/#output_file
```

## Assumption
1. Input location is on cluster and accessible from spark. if not we have to move file to location on cluster and path to be provided to spark application.

```
hadoop fs -put -f #local_linux_path #input_path_cluster
```

2. Output location is on cluster and accessible from spark.

3. Created single application for Both tasks.

4. In Task-2 I have filtered records with BEEF and printed results as it was not mentioned persist this result.

5. Created output file with difficulty,avg_total_cooking_time  with %BEEF% as filter. 
