# Clarify CLI

<!--markdownlint-disable MD026-->
<!--Deliberately adding punctuation to headers-->

<br>

## What is Clarify?

-----

Clarify is a Python CLI Utility specifically targeted to assist with making common tasks on the AWS cloud and other cloud providers as easy as possible. It is wrapper utility that clarifies service provider APIs by making them much easier to utilize.

<br>

## Why build another CLI Tool?

-----

There are dozens of command line tools available to perform all types of tasks for service provider APIs. The goal of clarify is to bridge the gap between some of these super useful tools and bring them all into a single command line interface to access these APIs in clear and concise ways to allow the tool to be used for a multitude of situations.

<br>

## What does Clarify currently do?

-----

Clarify currently has the following commands available to its ever list of growing options.

<br>

__Clarify Base CoreCommands:__

clarify --help

        clarify version
        clarify {SubCommand}

_keywords_map = {
    'Args:': 'Arguments',
    'Arguments:': 'Arguments',
    'Attributes:': 'Attributes',
    'Example:': 'Examples',
    'Examples:': 'Examples',
    'Keyword Args:': 'Arguments',
    'Keyword Arguments:': 'Arguments',
    'Methods:': 'Methods',
    'Note:': 'Notes',
    'Notes:': 'Notes',
    'Other Parameters:': 'Arguments',
    'Parameters:': 'Arguments',
    'Return:': 'Returns',
    'Returns:': 'Returns',
    'Raises:': 'Raises',
    'References:': 'References',
    'See Also:': 'See Also',
    'Todo:': 'Todo',
    'Warning:': 'Warnings',
    'Warnings:': 'Warnings',
    'Warns:': 'Warns',
    'Yield:': 'Yields',
    'Yields:': 'Yields',
  }

site_name: pyodoc-markdown Documentation
repo_url: https://github.com/NiklasRosenstein/pydoc-markdown
generate:
- document.md:
  - pydocmd.document++
- imp.md:
  - pydocmd.imp+
- extensions/loader.md:
  - pydocmd.loader++
- extensions/preprocessor.md:
  - pydocmd.preprocessor++
pages:
- Home: index.md << ../README.md
- API Documentation:
  - Document: document.md
  - Import Utils: imp.md
- Extension API:
  - Loader: extensions/loader.md
  - Preprocessor: extensions/preprocessor.md