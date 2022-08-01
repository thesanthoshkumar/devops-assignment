# devops-assignment

Monitoring is enabled for VM to check whether the VM status using the Compute Engine Google API's, 
If VM status is Terminated, Then It will alert the Cloud Pub/Sub Topic compute-engine-status.
Cloud Pub/Sub topic compute-engine-status will pull the message from the alert and triggers the CloudFunction.
CloudFunction will read the event to get details of the InstanceID , InstanceName, CreationTimestamp and LastStopTimestamp.
CloudFunction will write the event data to a csv file and puts the data.csv file to GCP CloudStorage
