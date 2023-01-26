import boto3
import logging
from cloudwatch_logging import CloudWatchLogHandler

cloudwatch_logs = boto3.client("logs")
s3 = boto3.client("s3")

log_group_name = ""
log_stream_name = ""
cloudwatch_logs.create_log_group(logGroupName=log_group_name)
cloudwatch_logs.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%m-%d %H:%M",
                    handlers=[CloudWatchLogHandler(log_group_name, log_stream_name, boto3.client("logs"))])

import boto3

def delete_from_s3(app, image_key, bucket_name):
    with app.app_context():
        try:
            s3 = boto3.client("s3")
            s3.delete_object(Bucket=bucket_name, Key=image_key)
            logging.info(f"Deleted image with key {image_key} from bucket {bucket_name}")
        except FileNotFoundError as e:
            logging.exception("Image cannot be found in S3: %s", e)
        except ValueError as e:
            logging.exception("Invalid key: %s", e)
        return None
