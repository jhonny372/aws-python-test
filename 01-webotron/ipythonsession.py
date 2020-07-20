# coding: utf-8
import boto3
session = boto3.Session(profile_name='janaTest')
s3 = session.resource('s3')

for bucket in s3.buckets.all():
    print(bucket)

#new_bucket = s3.create_bucket(
#    Bucket='jana-aws-test1',
#    CreateBucketConfiguration={
#        'LocationConstraint': 'us-west-1' })
#for bucket in s3.buckets.all():
#    print(bucket)

#new_bucket
