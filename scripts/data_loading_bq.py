from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig,SourceFormat

project_id='smooth-tesla-400908'
dataset_id='youtube_api_etl'
table_id='madras_samayal'
full_table_id=f'{project_id}.{dataset_id}.{table_id}'
file_path=r"data\processed\cleansed_video_data.csv"

def file_ingestion():
    job_config=LoadJobConfig(source_format=SourceFormat.CSV,skip_leading_rows=1,autodetect=True,write_disposition='WRITE_TRUNCATE')
    client=bigquery.Client(project=project_id)
    with open(file_path,'rb') as source:
        load_job=client.load_table_from_file(source,full_table_id,job_config=job_config)
    load_job.result()
    print('successfully loaded')

if __name__=='__main__':
    file_ingestion()