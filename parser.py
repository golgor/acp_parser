import os
import sys

def list_data_files():
    """Returns all folders in the data directory. If you
    folders are found, creates the data directory.

    Returns:
        list: Returns paths to all data files found in the /data-folder
    """
    data_files = list()

    data_dir = os.path.join(os.getcwd(),"data")
    for root, sub, files in os.walk(data_dir):
        file_list = [
            os.path.join(root, filename)
            for filename in files
            if "dacval" in filename
        ]
        # As "file_list" is a list we can't just append. In that case "data_files" will be a list of lists.
        # If we use unpacking we can "append" all elements in "file_list" to "data_files" instead of looping through.
        if file_list:
            data_files=[*data_files, *file_list]

    return data_files

def convert_to_int(byte_array, stride=2):
    """Converts a byte array to a list with specific integer values.
    Byte arrays is typically a sequence of hexadecimal values '\x00\x01\x00\x02'
    and with default values, this function splits this array to [1,2].

    Args:
        byte_array (bytearray): The byte array to be converted
        stride (int, optional): How many bytes per value, 2 for 32bit and 4 for 64bit. Defaults to 2.

    Returns:
        list: a list with all the converted bytes.
    """
    int_array=[
        int.from_bytes(byte_array[i:i+stride], byteorder='little', signed=True)
        for i
        in range(0, len(byte_array), stride)
    ]
    
    return int_array

def read_data(filename):
    '''Opening and reading file in binary mode.'''
    with open(filename, 'rb') as file:
        data = file.read()
    
    int_array = convert_to_int(data)
    return int_array

# funktion för att gå och läsa ur datan ur 
# funktion för göra om till rätt byte-format 32 eller 64 bitars