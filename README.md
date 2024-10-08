Flow Log Parser
Overview :
This program parses AWS VPC flow logs (version 2, default format) and generates two output files:

    Tag Counts: Number of occurrences for each tag.
    Port/Protocol Combination Counts: Number of occurrences for each port/protocol combination.

Assumptions

    Only default log format is supported (not custom).
    Only version 2 of flow logs is supported.
    Input files are in plain text format.
    Lookup table file is in CSV format with dstport, protocol, and tag columns.

Requirements

    Python 3.x (tested on Python 3.9)
    No external dependencies or packages required

Usage

    Clone this repository.
    Place flow log file (flow_log.txt) and lookup table file (lookup_table.csv) in the same directory.
    Run the program using python flow_log_parser.py.
    Output files will be generated in the same directory.

Compilation/Running
No compilation required. Run the program using Python interpreter.
Testing
The following tests are included:

    Verified that the parser generates correct tag counts and port/protocol combination counts.
    Verified that the parser handles empty flow logs correctly.
    Verified that the parser raises an error when encountering an invalid lookup table.


Code Analysis

    The program uses a dictionary to store lookup table data for efficient lookups.
    It iterates through each flow log record, updating tag counts and port/protocol combination counts accordingly.

Files

    flow_log_parser.py: Main program file.
    README.md: This file.
    flow_log.txt: Sample flow log file.
    lookup_table.csv: Sample lookup table file.
