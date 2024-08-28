#!/usr/bin/env python3

import boto3
import aws_cdk as cdk

from cdk_stacks.redshift_serverless_stack import RedshiftServerlessStack
from cdk_stacks.sagemaker_notebook_stack import SagemakerNotebookStack


app = cdk.App()

# Retrive AWS account ID and region
session = boto3.Session()
sts_client = session.client('sts')
account_id = sts_client.get_caller_identity()["Account"]
region = session.region_name

default_env = {
    "account": account_id,
    "region": region
};

redshift_admin_user = "<admin_user>"
redshift_admin_user_password = "<admin_user_password>"

redshift_credentials = {
    "admin_username": redshift_admin_user,
    "admin_user_password": redshift_admin_user_password
}

RedshiftServerlessStack(app, "RedshiftServerlessStack", redshift_credentials=redshift_credentials, env=default_env)
SagemakerNotebookStack(app, "SagemakerNotebookStack", env=default_env)

app.synth()
