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


def upload_to_s3(app, file, image_key, bucket_name, acl="public-read"):
    if file:
        try:
            key = image_key + file.filename
            s3.upload_fileobj(
                file, 
                bucket_name, 
                key, 
                ExtraArgs={
                    "ACL": acl,
                    "ContentType": file.content_type
                }
            )
        except FileNotFoundError as e:
            logging.exception("Error: File not Found %s", e)
        except ValueError as e:
            logging.exception("Invalid Key value: %s", e)
        return "{}{}".format(app.config["S3_LOCATION"], key)
    else:
        return app.config["S3_LOCATION"] + "default-image-filename"
