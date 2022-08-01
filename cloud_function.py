from wsgiref import headers
from google.cloud import storage
from pkg_resources import resource_filename
import csv

def write_data(event,context):
    header = ["InstanceID", "InstanceName", "CreationTimestamp", "LastStopTimestamp"]

    data =[{"InstanceID": event.Instanceid}, {"InstanceName": event.InstanceName}, {"CreationTimestamp":event.CreationTimestamp}, {"LastStopTimestamp": event.LastStopTimestamp}]

    with open('data.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f)

        # write the header
        writer.writeheader(header)

        # write multiple rows
        writer.writerows(data)

    def upload_blob(bucket_name, blob_text, destination_blob_name):
        """Uploads data to the bucket."""
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_string(blob_text)

        print('File {} uploaded to {}.'.format(
            resource_filename,
            destination_blob_name))

    def log_data(request):
        request_json = request.get_json()
        BUCKET_NAME = 'cloud-function-testing22'
        BLOB_NAME = 'data.csv'
        BLOB_STR = '{"blob": "some csv"}'

        upload_blob(BUCKET_NAME, BLOB_STR, BLOB_NAME)
        return f'Success!'
