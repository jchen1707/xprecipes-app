import boto3
import logging

class CloudWatchLogHandler(logging.Handler):
    def __init__(self, log_group, log_stream, boto3_client):
        logging.Handler.__init__(self)
        self.log_group = log_group
        self.log_stream = log_stream
        self.client = boto3_client
        self.sequence_token = None
    
    def emit(self, record):
        log_entry = self.format(record)
        self.client.put_log_events(
            logGroupName=self.log_group,
            logStreamName=self.log_stream,
            logEvents=[{
                "timestamp": int(record.created*1000),
                "message": log_entry
            }],
            sequenceToken=self.sequence_token
        )
