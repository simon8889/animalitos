from os import getenv
from fastapi import HTTPException, status
import boto3
from strawberry.file_uploads import Upload
from app.config import settings

class ImageUploadService:
	def __init__(self):
			self.bucket = settings.AWS_BUCKET
			self.s3_client = boto3.client(
				's3',
				aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
				aws_secret_access_key= settings.AWS_SECRET_ACCESS_KEY
			)
	
	async def upload(self, file_to_upload: Upload, filename: str):
		try:
			await file_to_upload.seek(0)
			self.s3_client.upload_fileobj(file_to_upload.file, self.bucket, f"{filename}")
		except Exception as e:
			raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error")