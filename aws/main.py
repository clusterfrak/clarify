##############################################################################
# Clarify CLI: Clarify() Class
#====================================================================
# Main Clarify Command Class
#
# Author: Richard Nason rnason@clusterfrak.com
# Project Start: 08/24/2019
# License: GNU GPLv3
##############################################################################

###############
# Imports:
###############
# PIP Install required imports
import boto3
from botocore.exceptions import ClientError
from colorama import init

# Import AWS service class's
from clarify.utils import ClarifyUtils
from aws.s3 import ClarifyS3

# Import Std Python modules
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()


#####################
# Clarify() Class:
#####################

class Clarify(object):
    """
    Python CLI Utility specifically targeted to assist with performing common tasks on the AWS cloud and other cloud providers as easy as possible. It is a
    wrapper utility that clarifies service provider APIs.

    Usage:
        clarify --help
        clarify version
        clarify {SubCommand}
        clarify --profile dev --region us-east-1 {SubCommand}

    Available Subcommands:
        util:       Set of helper functions to perform various functions.
        s3:         Set of AWS S3 commands that allow simplified usage of common s3 actions
        codebuild:  Set of AWS CodeBuild commands to help with project pipelines
    """
    
    
    def __init__(self, profile='default', region='us-east-1'):
        """
        Instantiation point for the main Clarify() Class

        Args:
            profile (string): Name of an aws profile to use. 'default' profile is used unless specified. [~/.aws/credentials, ~/.aws/config]
            region (string):  Default region to use when creating new connection to one of the available AWS services.

        Returns: None
        TODO: Inject AMSCM and AMSSKMS service definitions into the environment.
        """
        # Set AWS default profile and region
        self.profile = profile
        self.region = region
        
        # Import ClarifyUtils
        self.util = ClarifyUtils()

        # Set Initial AWS Session
        session = boto3.session.Session(profile_name=self.profile, region_name=self.region)

        # Import AWS service classes
        self.s3 = ClarifyS3(session)



    def version(self):
        """
        Returns the semantic version of clarify.

        Usage:
            clarify version
            clarify version --help

        Args: None
        
        Return: Clarify CLI Version x.x.x
        """
        version = "0.0.1"
        response = colored("\nClarify CLI Version: ", 'blue') + colored(version, 'red') + "\n"
        return response



