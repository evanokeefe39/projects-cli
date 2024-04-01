from prefect import flow, task, get_run_logger
from prefect_aws import AwsCredentials

aws_credentials_block = AwsCredentials.load("test-wp-creds")

@task(name='Extract')
def extract():
    return 'extracted data'


@task(name='Transform')
def transform(data):
    return data.upper()


@task(name='Load')
def load(data):
    print(data)

@flow(name='ETL', retries=2)
def create_flow():

    logger = get_run_logger()
    logger.info('Creating flow run')

    data = extract()

    transformed_data = transform(data)

    load(transformed_data)
    logger.info('Flow run complete')
    