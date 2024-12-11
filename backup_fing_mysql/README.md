# Backup-to-S3

A Python-based script to periodically back up data from the Fing API to an S3-compatible storage service. This project uses `aiohttp` for making asynchronous HTTP requests and `aiobotocore` to interact with S3 storage.

## Features

- Fetches the latest backup from the Fing API.
- Downloads the backup file.
- Uploads the backup file to an S3 bucket.
- Runs continuously, fetching new backups every hour.

## Prerequisites

- Python 3.13 or later.
- An S3-compatible storage service (e.g., AWS S3, MinIO).
- Fing API credentials (email and password).

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>


Build the Docker image:

bash
Copy code
docker build -t backup-to-s3 .
Run the container:

bash
Copy code
docker run -e ACCESS_KEY=<your-access-key> \
           -e SECRET_KEY=<your-secret-key> \
           -e ENDPOINT_URL=<s3-endpoint-url> \
           -e BUCKET_NAME=<bucket-name> \
           -e SERVICE_NAME=<service-name> \
           -e FING_EMAIL=<email> \
           -e FING_PASSWORD=<password> \
           -t backup-to-s3
Environment Variables
ACCESS_KEY: Your S3 access key.
SECRET_KEY: Your S3 secret key.
ENDPOINT_URL: The S3-compatible service endpoint URL.
BUCKET_NAME: Name of the S3 bucket where backups will be stored.
SERVICE_NAME: Name of the Fing service whose backups will be fetched.
FING_EMAIL: Email address for the Fing API.
FING_PASSWORD: Password for the Fing API.
Project Structure
bash
Copy code
.
├── main.py         # The main script to perform the backup process.
├── Dockerfile      # Dockerfile to containerize the application.
├── README.md       # Project documentation (this file).
How It Works
Logs into the Fing API to retrieve an access token.
Fetches the latest backup information for the specified service.
Downloads the backup file using the provided download link.
Uploads the backup file to the configured S3 bucket.
Repeats the process every hour.
Requirements
The script installs the following dependencies:

aiohttp: For making asynchronous HTTP requests.
aiobotocore: For interacting with S3 in an asynchronous manner.
These dependencies are listed in the Dockerfile and will be installed during the build process.

Notes
Ensure the S3 bucket is created before running the script.
Make sure your Fing API credentials and S3 keys are valid and have the necessary permissions.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
