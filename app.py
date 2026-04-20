import boto3
import subprocess
import os

s3 = boto3.client(
    "s3",
    aws_access_key_id     = os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"],
    region_name           = "us-east-1"
)
s3.download_file("spitzkop-marketing", "spitzkop_jobs.db", "/app/spitzkop_jobs.db")
print("Base téléchargée depuis S3")

subprocess.run([
    "datasette", "serve",
    "/app/spitzkop_jobs.db",
    "--host", "0.0.0.0",
    "--port", "8080",
    "--cors",
    "--setting", "max_returned_rows", "10000",
])
