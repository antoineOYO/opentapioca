# Import necessary libraries
import bz2
import json
import sys
from opentapioca.wditem import WikidataItemDocument

# Class definition for WikidataDumpReader
class WikidataDumpReader(object):
    """
    Generates a stream of `WikidataItemDocument` from
    a Wikidata dump.
    """

    # Constructor to initialize the object with a file name
    def __init__(self, fname):
        # Store the file name as an instance variable
        self.fname = fname
        # Check if the file name is '-' (stdin), and set the file object accordingly
        if fname == '-':
            self.f = sys.stdin
        else:
            # If not stdin, open the file using bz2 for reading text with utf-8 encoding
            self.f = bz2.open(fname, mode='rt', encoding='utf-8')

    # Context manager method for entering a 'with' block
    def __enter__(self):
        return self

    # Context manager method for exiting a 'with' block
    def __exit__(self, *args, **kwargs):
        # Close the file if it is not stdin
        if self.fname != '-':
            self.f.close()

    # Iterator method allowing iteration over the lines of the file
    def __iter__(self):
        # Iterate over each line in the file
        for line in self.f:
            try:
                # Remove the trailing comma from the line if present
                if line.rstrip().endswith(','):
                    line = line[:-2]
                # Parse the line as JSON and create a WikidataItemDocument object
                item = json.loads(line)
                yield WikidataItemDocument(item)
            except ValueError as e:
                # Handle the case where a line cannot be parsed as JSON (e.g., at the beginning or end of dumps)
                continue
