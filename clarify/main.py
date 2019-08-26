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
# from clarify.utils import ClarifyUtils

# Import Std Python modules
from termcolor import colored
import ntpath

# use Colorama to make Termcolor work on Windows too
init()


#####################
# Clarify() Class:
#####################

class Clarify(object):
    """Clarify Class that constructs the core clarify CLI

    ...

    Attributes
    ----------
    command_output : {str}
        The final output of the command back to the user
    filepath : {str}
        The full path to a file such as /var/lib/another/folder/file.ext
    path : {bool}
        Flag to indicate the return the path instead of the filename from the provided input (default false)

    Methods
    -------
    version()
        Returns the semantic version of clarify
    fetch(filepath=None, path=False)
        Split a provided filepath and return back only the filename or path

    Todo
    ----
        Add additional AWS support
        Add Github support
        Add Bitbucket support
        Add BuildSpec support
        Add Jenkins support
        Add Config File Support
        Add AWS Assume Role support
        Add AWS Assume Role with MFA support
        Add AWS Assume Role with SAML support
        Inject AMSCM and AMSSKMS service definitions into the environment.
        TBD...
    """

    command_output = "\n {output} \n"
    
    def __init__(self, filepath=None, path=False):
        """
        Python CLI Utility specifically targeted to assist with performing common tasks on the AWS cloud and other cloud providers as easy as possible. It is a
        wrapper utility that clarifies service provider APIs for a more streamlined consumption experience.

        Parameters
        ----------
        filepath : {str}
            The full path to a file such as /var/lib/another/folder/file.ext
        path : {bool}
            Flag to indicate the return the path instead of the filename from the provided input (default false)
        """

        # Define class constructor internal variables
        self.clarify_version = "0.0.1"

        # Define class constructor class input variables
        self.filepath = filepath
        self.path = path

        # Import AWS service classes
        # self.s3 = ClarifyS3(session)


    def version(self):
        """Returns the semantic version of clarify

        The version subcommand simply returns back the running version of the clarify CLI.
        To learn about all of the available options for the version command type: 
        clarify version --help

        Parameters
        ----------
        None

        Raises
        ------
        NotImplementedError
            If no version variable is set or available within the class.

        Returns
        ------
        str
            Semantic version of clarify

        Examples
        --------
            clarify version
            Output: Clarify CLI Version 0.0.1
        """

        if self.clarify_version is None:
            raise NotImplementedError("Version unset, or unavailable to the clarity class constructor!")

        version = colored("Clarify CLI Version: ", 'blue') + colored(self.clarify_version, 'red')
        return self.command_output.format(output=version)


    def fetch(self, filepath, path=False):
        """Split a given filepath and return back only the filename or path

        The fetch subcommand takes a provided file path and returns back only the filename portion of the filepath path.
        If the --path flag is provided to the command, then only the path instead of the filename is returned as the output.
        To learn about all of the available options for the fetch command type: 
        clarify fetch --help

        Parameters:
        ----------
        filepath : {str}
            The full path to a file such as /var/lib/another/folder/file.ext
        path : {bool}
            Flag to indicate the return the path instead of the filename from the provided input (default false)

        Raises
        ------
        NotImplementedError
            If no filepath value is provided or available within the class

        Returns
        ------
        {str}
            String containing either the file Name or Path depending on if the `--path` flag was passed (e.g. file.ini, /var/lib)

        Examples
        --------
            clarify fetch /path/to/file.ini
            Output: file.ini


            clarify fetch /path/to/file.ini --path
            clarify fetch --filepath /path/to/file.ini -path
            Output: /path/to

        Notes
        -----
            The --filepath argument (/path/to/some/file) is a required parameter.
        """

        if self.filepath is None and filepath is None:
            raise NotImplementedError("Value for filepath expected but no value was given! Please try the command again using a valid filepath")

        try:
            # Set the variable value for variable filepath and path
            # Setting the values with if statements allows the option of the 
            # class being consumed by another function.
            filepath_local = self.filepath if filepath is None else filepath
            path_local     = self.path if not path else path

            # Separate the path from the filename and store in separate variables       
            given_path, given_filename = ntpath.split(filepath_local)
            
            # Check the flag and set the appropriate return value
            if path_local:
                return_value = given_path
            else:
                return_value = given_filename or ntpath.basename(given_path)
        except Exception as e:
            return_value = colored("Error: An unexpected error has been encountered attempting to split the given filepath: {} \n {}".format(filepath, str(e)), 'red')

        result = return_value if "Error" in return_value else colored(return_value, 'blue')
        return self.command_output.format(output=result)
