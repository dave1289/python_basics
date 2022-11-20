import os

def read_file_list(filename):
    txt_file = open(filename, 'r')
    data = txt_file.readlines()
    no_break = []
    for entry in data:
        no_break.append(entry.replace('\n', ''))
    for entry in no_break:
        print('-' + entry)

    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!