import aiohttp, asyncio, io, aiobotocore.session, botocore.config
access_key, secret_key, endpoint_url, bucket_name, service_name = "", "", "", ""
async def main():
    while True:
        session = aiobotocore.session.get_session()
        async with session.create_client('s3',aws_access_key_id=access_key,aws_secret_access_key=secret_key,endpoint_url=endpoint_url,config=botocore.config.Config(signature_version="s3v4")) as s3_client:
            try:
                async with aiohttp.ClientSession() as http_session:
                    token = (await(await http_session.post('https://api.fing.ir/v1/user/login', json={'email': '','password': ''})).json())["token"]
                    last_backup = (await(await http_session.get(f'https://api.fing.ir/v1/apps/{service_name}/backups', headers={'authorization': f'Bearer {token}'})).json())[-1]
                    download_link = (await(await http_session.get(f'https://api.fing.ir/v1/apps/{service_name}/backups/{last_backup["id"]}/download', headers={'authorization': f'Bearer {token}'})).json())["url"]
                    async with http_session.get(download_link) as response: await s3_client.put_object(Bucket=bucket_name,Key=f"{last_backup['created_at']}.tar.gz",Body=io.BytesIO(await response.read()).getvalue())
            except Exception as e:print(f"An error occurred: {e}")
        await asyncio.sleep(3600)
if __name__ == "__main__":asyncio.run(main())
