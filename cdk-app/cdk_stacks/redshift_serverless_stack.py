from aws_cdk import (
    Stack,
    aws_redshiftserverless as redshiftserverless
)
from constructs import Construct

class RedshiftServerlessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, redshift_credentials: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        admin_user_password = redshift_credentials['admin_user_password']
        admin_username = redshift_credentials['admin_username']
        
        # Create a Redshift Serverless namespace
        namespace = redshiftserverless.CfnNamespace(
            self, "MyNamespace",
            namespace_name="cdk-namespace",
            admin_user_password=admin_user_password,  # Replace with a secure password
            admin_username=admin_username,
        )

        # Create a Redshift Serverless workgroup
        workgroup = redshiftserverless.CfnWorkgroup(
            self, "MyWorkgroup",
            workgroup_name="cdk-workgroup",
            namespace_name=namespace.ref,
            base_capacity=32,  # Minimum Base Capacity in Seoul Region
        )
