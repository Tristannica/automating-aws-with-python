import boto3
import sys

session = boto3.Session(profile_name='pyauto')
s3 = session.resource('s3')

if __name__ == '__main__':
    for bucket in s3.buckets.all():
        print(bucket)
