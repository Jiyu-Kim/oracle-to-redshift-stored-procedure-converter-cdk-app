#!/usr/bin/env python3
import os
from dotenv import load_dotenv

import aws_cdk as cdk

from cdk_stacks.redshift_serverless_stack import RedshiftServerlessStack
from cdk_stacks.sagemaker_notebook_stack import SagemakerNotebookStack


app = cdk.App()

default_env = {
    "account": os.getenv("ACCOUNT"),
    "region": os.getenv("REGION_NAME", "us-west-2")
};

redshift_admin_user = "<admin_user>"
redshift_admin_user_password = "<admin_user_password>"

redshift_credentials = {
    "admin_username": redshift_admin_user,
    "admin_user_password": redshift_admin_user_password
}

RedshiftServerlessStack(app, "RedshiftServerlessStack", redshift_credentials=redshift_credentials, env=default_env)
SagemakerNotebookStack(app, "SagemakerNotebookStack")

app.synth()
