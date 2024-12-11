import aiohttp
import asyncio
import io
import aiobotocore.session
import botocore.config
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch variables from the environment
access_key = os.getenv("ACCESS_KEY")
secret_key = os.getenv("SECRET_KEY")
endpoint_url = os.getenv("ENDPOINT_URL")
bucket_name = os.getenv("BUCKET_NAME")
service_name = os.getenv("SERVICE_NAME")
email = os.getenv("FING_EMAIL")
password = os.getenv("FING_PASSWORD")

async def main():
    while True:
        session = aiobotocore.session.get_session()
        async with session.create_client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            endpoint_url=endpoint_url,
            config=botocore.config.Config(signature_version="s3v4")
        ) as s3_client:
            try:
                async with aiohttp.ClientSession() as http_session:
                    # Login to Fing API
                    token = (await (await http_session.post(
                        'https://api.fing.ir/v1/user/login',
                        json={'email': email, 'password': password}
                    )).json())["token"]

                    # Get the latest backup
                    last_backup = (await (await http_session.get(
                        f'https://api.fing.ir/v1/apps/{service_name}/backups',
                        headers={'authorization': f'Bearer {token}'}
                    )).json())[-1]

                    # Get the download link
                    download_link = (await (await http_session.get(
                        f'https://api.fing.ir/v1/apps/{service_name}/backups/{last_backup["id"]}/download',
                        headers={'authorization': f'Bearer {token}'}
                    )).json())["url"]

                    # Download and upload the backup
                    async with http_session.get(download_link) as response:
                        await s3_client.put_object(
                            Bucket=bucket_name,
                            Key=f"{last_backup['created_at']}.tar.gz",
                            Body=io.BytesIO(await response.read()).getvalue()
                        )
            except Exception as e:
                print(f"An error occurred: {e}")
        
        # Wait for an hour before the next backup
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
