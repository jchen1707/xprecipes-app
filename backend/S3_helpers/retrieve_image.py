import boto3
import logging
from cloudwatch_logging import CloudWatchLogHandler
from backend.config import ACCESS_KEY_ID, SECRET_ACCESS_KEY


session = boto3.Session(
    aws_access_key_id= ACCESS_KEY_ID,
    aws_secret_access_key= SECRET_ACCESS_KEY
)
s3 = session.client("s3")
cloudwatch_logs = session.client("logs")

log_group_name = "xprecipes-logs"
log_stream_name = "xprecipes-log_stream"
cloudwatch_logs.create_log_group(logGroupName=log_group_name)
cloudwatch_logs.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%m-%d %H:%M",
                    handlers=[CloudWatchLogHandler(log_group_name, log_stream_name, boto3.client("logs"))])

def get_image_url(image_key, bucket_name):
    try:
        url = s3.generate_presigned_url("get_object",
                                        Params={"Bucket": bucket_name,
                                                "Key": image_key},
                                        ExpiresIn=3600)
        return url
    except FileNotFoundError as e:
        logging.exception("Image cannot be found in S3: %s", e)
    except ValueError as e:
        logging.exception("Invalid key: %s", e)
        return None
