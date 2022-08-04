"""An AWS Python Pulumi program"""
import json
import pulumi
from pulumi_aws import iam

mybadPolicy = iam.Policy('my-bad-policy',
                         name='my-bad-policy',
                         path='/',
                         description='A bad IAM Policy',
                         policy=json.dumps({
                             "Version": "2012-10-17",
                             "Statement": [{
                                 "Sid": "VisualEditor0",
                                 "Effect": "Allow",
                                 "Action": [
                                     "s3:GetBucketObjectLockConfiguration",
                                     "s3:DeleteObjectVersion",
                                     "s3:DeleteBucket"
                                 ],
                                 "Resource": "*"
                             }]
                         })
                         )

# Export the name of the bucket
pulumi.export('policy_arn', mybadPolicy.arn)
