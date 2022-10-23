import io
from boto3 import Session
import pandas as pd

aws = Session(
    aws_access_key_id='aws access key',
    aws_secret_access_key='aws secret key'
)

excelObject = aws.resource('s3').Bucket('bucket name').Object('excel filename.xlsx').get()
excelFile = io.BytesIO(excelObject['Body'].read())

df = pd.read_excel(excelFile, engine='openpyxl')

print(df)