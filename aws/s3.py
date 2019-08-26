###############
# Imports:
###############
# Import Pip Installed modules
from colorama import init

# Import AWS service class's
from clarify.utils import ClarifyUtils

# Import STD Python modules
import os
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()


class ClarifyS3(object):
    """
    Simplified commands that interface with the Amazon S3 service

    Usage:
        clarify s3 --help
        clarify s3 {SubCommand}
        clarify s3 --bucket myBucket {SubCommand}

    Available Subcommands:
        upload:  Uploads a file or folder to a specified Amazon S3 bucket
    """


    def __init__(self, session, expiration_time=72, expiration_format='H'):
        """
        Instantiation point for the clarify ClarifyS3() Class

        Args:
            session (object): The AWS session state instantiated from calling clarify

        Returns: None
        """
        # Import Modules
        self.utils = ClarifyUtils()

        # Set the S3 connector objects
        self.s3Resource = session.resource('s3')
        self.s3Client   = session.client('s3')


    def upload(self, path, bucket, s3key=None):
        """
        Uploads a file or folder to a specified Amazon S3 bucket

        Description:
          Provide either a path to a file or directory to upload to the specified S3 bucket. If --s3key is not specified file will retain same name when copied.

        Usage:
            clarify s3 upload --help
            clarify s3 upload /var/lib/somedir/config.file myS3Bucket
            clarify s3 upload --path /var/lib/somedir/config.file  --bucket myS3Bucket
            clarify s3 upload --bucket myS3Bucket --path /var/lib/somedir/config.file
            clarify s3 upload --bucket myS3Bucket --path /var/lib/somedir/config.file --s3key newfile.name
            clarify s3 upload --bucket myS3Bucket /var/lib/somedir
            clarify s3 upload --bucket myS3Bucket --path /var/lib/somedir

        Args:
            bucket (string):  Name of the bucket to upload the specified files/folder to (REQUIRED)
            path (string):    The path to the file or directory to upload to the specified S3 bucket
            s3key (string):   The name that the file will be changed to when copied to S3 If no value specified, file will retain its original name (OPTIONAL)

        Return:
            Success/Failure message of upload attempt

        TODO: Support Encryption
        TODO: Allow Storage of Encryption and KMS Key Id, etc in a config file
        TODO: Pass the provided region to the function.
        """
        # Make sure that a bucket was provided
        if bucket:
            # Get just the filename from the provided filename input in the event that a path was received.
            try:
                if s3key is None:
                    s3key = self.utils.splitpath(path)
            except Exception as e:
                print(colored("\nERROR: An unexpected error occurred when attempting to fetch the filename from the provided path", 'red'))
                print(str(colored(e, 'yellow'))+ "\n")
            
            # Check to see if the provided path is a file or directory and upload
            try:
                if os.path.isfile(path):
                    self.s3Resource.Bucket(bucket).upload_file(path, s3key)
                    print(colored("\n" + bucket + "/" + s3key + " uploaded successfully!\n", 'green'))
                elif os.path.isdir(path):
                    print("\n")
                    for root,dirs,files in os.walk(path):
                        for file in files:
                            self.s3Resource.Bucket(bucket).upload_file(os.path.join(root,file), file)
                            print(colored(bucket + "/" + file + " uploaded successfully!", 'green'))
                    print("\n")
            except Exception as e:
                print(colored("\nERROR: An unexpected error occurred when attempting upload the specified file", 'red'))
                print(str(colored(e, 'yellow'))+ "\n")
        else:
            print(colored("\nERROR: A bucket must be provided in order to use this command. Please check the command using --help or specify a bucket and try again."), 'red')
            print(colored("clarify s3 upload --bucket myS3Bucket --path /var/lib/somedir/config.file --s3key newfile.name\n"), 'blue')
        
    
    
    
    
    
    # def psurlExpiration(self):
    #     '''Simple function to calculate the requested expiration of the pre-signed URL'''
    #     # Calculate the expiration time of the pre-signed URL
    #     if self.psurl_timeout_format == 'S':
    #         self.psurl_expiration = int(self.psurl_timeout)
    #     elif self.psurl_timeout_format == 'M':
    #         self.psurl_expiration = int(self.psurl_timeout) * 60
    #     elif self.psurl_timeout_format == 'H':
    #         self.psurl_expiration = (int(self.psurl_timeout) * 60) * 60
    #     elif self.psurl_timeout_format == 'D':
    #         self.psurl_expiration = ((int(self.psurl_timeout) * 60) * 60) * 24
    #     return self.psurl_expiration


    #     '''Clarify AWS S3 Class.

    #     simplified functions that interface with
    #     # the Amazon S3 service via Boto3.

    #     This Class contains methods that pertain to the Amazon
    #     AWS S3 service. Common functions will be included in this
    #     class in order to simplify the interaction with Amazon S3.
    #     '''

    #     # Set Class variables
    #     self.bucket               = bucket
    #     self.filename             = filename
    #     self.s3_key               = s3_filename
    #     self.psurl_timeout        = expiration_time
    #     self.psurl_timeout_format = expiration_format

        


    
    

    # def psurl(self):
    #     '''Function to create a pre-signed URL from an uploaded S3 object'''
        
    #     # Once the file has been uploaded, create the pre-signed URL
    #     pre_signed_url = self.s3Client.generate_presigned_url(
    #         'get_object',
    #         Params={
    #             "Bucket": self.bucket,
    #             "Key": self.s3_key
    #         },
    #         ExpiresIn=self.psurlExpiration()
    #     )

    #     Output = "\n" + str(self.bucket) + "/" + str(self.s3_key) + " Pre-Signed URL:\n" + \
    #         "=========================================================================================\n" +\
    #         pre_signed_url + "\n"
    #     return Output


    
