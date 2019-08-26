###############
# Imports:
###############
# Import AWS service class's
# from clarify.utils import ClarifyUtils

# Import STD Python modules
import os


class ClarifyBuildSpec(object):
    """
    Command groups that can be used in conjunction with CodeBuild buildspec files. 

    Usage:
        clarify buildspec --help
        clarify buildspec {SubCommand}
        clarify buildspec --bucket myBucket {SubCommand}

    Available Subcommands:
        upload:  Uploads a file or folder to a specified Amazon S3 bucket
    """


    def __init__(self, session):
        """
        Instantiation point for the clarify ClarifyBuildSpec() Class

        Args:
            session (object): The AWS session state instantiated from calling clarify

        Returns: None
        """
        # Import Modules
        # self.utils = ClarifyUtils()

        # Set the S3 connector objects
        # self.s3Resource = session.resource('s3')
        # self.s3Client   = session.client('s3')


    def upload(self, bucket, path, s3key=None):
        """
        Uploads a file or folder to a specified Amazon S3 bucket

        Description:
          Provide either a path to a file or directory to upload to the specified S3 bucket. If --s3key is not specified file will retain same name when copied.

        Usage:
            clarify s3 upload --help
            clarify s3 upload --bucket myS3Bucket /var/lib/somedir/config.file
            clarify s3 upload myS3Bucket /var/lib/somedir/config.file config.ini
            clarify s3 upload --bucket myS3Bucket --path /var/lib/somedir/config.file
            clarify s3 upload --bucket myS3Bucket --path /var/lib/somedir/config.file --s3key newfile.name
            clarify s3 upload --bucket myS3Bucket /var/lib/somedir
            clarify s3 upload --bucket myS3Bucket --path /var/lib/somedir

        Args:
            bucket (string):  Name of the bucket to upload the specified files/folder to (REQUIRED)
            path (string):    The path to the file or directory to upload to the specified S3 bucket
            s3key (string):   The name that the file will be changed to when copied to S3 (OPTIONAL) If no value specified, file will retain its original name

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
                print("An unexpected error occurred when attempting to fetch the filename from the provided path {}".format(str(e)))
            
            # Check to see if the provided path is a file or directory and upload
            # try:
            #     if os.path.isfile(path):
            #         upload_object = self.s3Resource.Bucket(bucket).upload_file(path, s3key)
            #         print(upload_object)
            #     elif os.path.isdir(path):
            #         for root,dirs,files in os.walk(path):
            #             for file in files:
            #                 upload_object = self.s3Resource.Bucket(bucket).upload_file(os.path.join(root,file), file)
            #                 print(upload_object)
            # except Exception as e:
            #     print("An unexpected error occurred when attempting to fetch the filename from the provided path {}".format(str(e)))
        else:
            print("A bucket must be provided in order to use this command. Please check the command using --help or specify a bucket and try again.")
            print("clarify s3 upload --bucket myS3Bucket --path /var/lib/somedir/config.file --s3key newfile.name")
