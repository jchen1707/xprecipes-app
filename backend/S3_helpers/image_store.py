import boto3 
import logging
from cloudwatch_logging import CloudWatchLogHandler

cloudwatch_logs = boto3.client('logs')
s3 = boto3.client('s3')

log_group_name = ""
log_stream_name = ""
cloudwatch_logs.create_log_group(logGroupName=log_group_name)
cloudwatch_logs.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%m-%d %H:%M',
                    handlers=[CloudWatchLogHandler(log_group_name, log_stream_name, boto3.client('logs'))])


def upload_to_s3(app,file,bucket_name, acl="public-read"):
    try:

        s3.upload_fileobj(
            file, 
            bucket_name, 
            file.filename, 
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    
    except FileNotFoundError as e:
        logging.exception("Error: File not Found %s", e)
    except ValueError as e:
        logging.exception("Invalid value: %s", e)

    
    return "{}{}".format(app.config["S3_LOCATION"], file.filename)