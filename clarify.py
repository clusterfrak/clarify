##############################################################################
# Clarify CLI:
#====================================================================
# Python CLI Utility specifically targeted to assist with making common tasks
# on the AWS cloud and other cloud providers as easy as possible.
# It is wrapper utility that clarifies service provider APIs by making
# them much easier to utilize.

# Author: Richard Nason rnason@clusterfrak.com
# Project Start: 08/24/2019
# License: GNU GPLv3
##############################################################################

###############
# Imports:
###############
# PIP Install required imports
import fire

# Import Main class
# from clarify.main import Clarify
from clarify.main import Clarify as clarify

if __name__ == "__main__":
    fire.Fire(clarify)
