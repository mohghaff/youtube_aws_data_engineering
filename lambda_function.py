import os
import pandas as pd
import urllib.parse
import awswrangler as wr


# Retrieve environment variables
s3_cleansed_layer = os.environ['s3_cleansed_layer']
glue_catalog_db_name = os.environ['glue_catalog_db_name']
glue_catalog_table_name = os.environ['glue_catalog_table_name']
write_data_operation = os.environ['write_data_operation']

# Lambda function handler
def lambda_handler(event, context):
    # Get the object details from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        # Read JSON data from S3 into a DataFrame
        df_raw = wr.s3.read_json('s3://{}/{}'.format(bucket, key))

        # Extract required columns
        df_step_1 = pd.json_normalize(df_raw['items'])

        # Write processed data to S3 and Glue Catalog
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=s3_cleansed_layer,
            dataset=True,
            database=glue_catalog_db_name,
            table=glue_catalog_table_name,
            mode=write_data_operation
        )

        return wr_response

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
