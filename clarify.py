#####################################################################
# Clarify is a Python CLI Utility specifically targeted to 
# assist with performing common tasks on AWS cloud as easy as
# possible. It is a wrapper and enhancement tool for the AWS CLI.
#####################################################################

###############
# Imports:
###############
# PIP Install required imports
import fire

# Import Main class
# from clarify.main import Clarify
from clarify import main

if __name__ == "__main__":
    clarify = main.Clarify()
    fire.Fire(clarify)
