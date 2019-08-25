###############
# Imports:
###############
# Std Py imports
import ntpath


class ClarifyUtils(object):
    """
    Helper functions that are included for the clarify CLI and available as SubCommands using: clarify util {SubCommand}

    Usage:
        clarify util --help
        clarify util {SubCommand}

    Available Subcommands:
        splitpath:  Takes a passed file path (/var/lib/file1) and returns only the filename, stripping the path (file1)
    """


    def __init__(self):
        """
        Instantiation point for the clarify ClarifyUtils() Class

        Args: None

        Returns: None
        """


    def splitpath(self, filepath):
        """
        Takes a passed file path (/var/lib/file1) and returns only the filename, stripping the path (file1)

        Usage:
            clarify util splitpath --help
            clarify util splitpath /var/lib/somedir/config.file
            clarify util splitpath --filepath /var/lib/somedir/config.file

        Args:
            filepath (string): Full path to a file where the desired return is simply the filename

        Return:
            config.file (or any filename that was passed at the end of the provided path)
        """
        # Split the path from the file name and just return the file name.        
        head, tail = ntpath.split(filepath)
        return tail or ntpath.basename(head)
    
