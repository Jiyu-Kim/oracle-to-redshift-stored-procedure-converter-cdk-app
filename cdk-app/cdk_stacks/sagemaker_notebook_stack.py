from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_sagemaker as sagemaker,
    CfnOutput,
    Fn,
)
from constructs import Construct
import os

class SagemakerNotebookStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # IAM Role
        SageMakerNotebookinstanceRole = iam.Role(
            self,
            "SageMakerNotebookInstanceRole",
            assumed_by=iam.ServicePrincipal("sagemaker.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonBedrockFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSageMakerFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonRedshiftFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
            ],
        )

        # SageMaker Notebook Instance Lifecycle Configuration
        #current_dir = os.path.dirname(os.path.realpath(__file__))
        #on_create_script_path = os.path.join(current_dir, "install_packages.sh")

        #with open(on_create_script_path, "r") as f:
        #    on_create_script_content = f.read()


        #cfn_notebook_instance_lifecycle_config = sagemaker.CfnNotebookInstanceLifecycleConfig(
        #    self,
        #    "MyCfnNotebookInstanceLifecycleConfig",
        #    notebook_instance_lifecycle_config_name="notebookInstanceLifecycleConfig",
        #    on_create=[
        #        {
        #            "content": Fn.base64(on_create_script_content),
        #        }
        #    ],
        #    on_start=[],
        #)

        # SageMaker Notebook Instance
        cfn_notebook_instance = sagemaker.CfnNotebookInstance(
            self,
            "MyCfnNotebookInstance",
            instance_type="ml.t3.medium",
            role_arn=SageMakerNotebookinstanceRole.role_arn,
            default_code_repository="https://github.com/Jiyu-Kim/stored-procedure-converter.git",
            direct_internet_access="Enabled",
            #lifecycle_config_name="notebookInstanceLifecycleConfig",
            notebook_instance_name="stored-procedure-converter-notebook",
            volume_size_in_gb=10,
        )