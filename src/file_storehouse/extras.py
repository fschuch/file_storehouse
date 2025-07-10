"""Extra utilities from external packages."""

from boto3 import client
from botocore.stub import Stubber

__all__ = [
    "client",
    "Stubber",
]
