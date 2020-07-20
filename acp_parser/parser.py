import os
from pathlib import Path


class DataFolder:
    def __init__(self, path, title):
        self.path = path
        self.title = title

        self.data_files = []

        for file in path.iterdir():
            self.data_files.append(DataFile(file))

    def get_title(self):
        return self.title


class DataFile:
    def __init__(self, path):
        self.path = path
        self.name = path.name

        if 'dacval' in self.name:
            self.type = "data"
        elif 'format' in self.name:
            self.type = "format"
        elif 'tick' in self.name:
            self.type = "tick"


class Parser:
    """[summary]
    """
    def __init__(self, location: str = None) -> None:
        """[summary]

        :param location: [description], defaults to None
        :type location: str, optional
        """
        if not location:
            location = os.getcwd()

        # Resolve absolute path to given folder.
        self.location = Path(location).resolve()
        self.data_folders = []

        # Scan for folder containing data files.
        # Append to list with DataFolder objects.
        self._scan(self.location)

    def _scan(self, search_path) -> list:
        """[summary]

        :param search_path: [description]
        :type search_path: [type]
        :return: [description]
        :rtype: list
        """
        for root, sub, files in os.walk(search_path):
            root_path = Path(root)

            # Skip subdirectories that are more than three levels deep.
            # This avoids crashing the script in case root of filesystem
            # is given as input.
            if (len(root_path.parts) - len(search_path.parts)) > 2:
                continue

            # If a file with 'dacval' contained in the name,
            # append a DataFolder instance for each data folder found.
            for file in files:
                if 'dacval' in file:
                    self.data_folders.append(
                        DataFolder(root_path, title=root_path.parts[-2])
                    )
                    break

    def get_data_folders(self):
        return self.data_folders


def list_data_files(path: str) -> list:
    """Returns all folders in the data directory. If you
    folders are found, creates the data directory.

    Returns:
        list: Returns paths to all data files found in the /data-folder
    """
    data_files = list()

    data_dir = os.path.abspath(path)
    for root, sub, files in os.walk(data_dir):
        # Skip subdirectories that are more than three levels deep.
        # This avoids crashing the script in case root of filesystem
        # is given as input.
        if (root.count(os.sep) - data_dir.count(os.sep)) > 3:
            continue

        file_list = [
            os.path.join(root, filename)
            for filename in files
            if "dacval" in filename
        ]
        # As "file_list" is a list we can't just append.
        # In that case "data_files" will be a list of
        # lists. If we use unpacking we can "append" all
        # elements in "file_list" to "data_files"
        # instead of looping through.
        if file_list:
            data_files = [*data_files, *file_list]

    return data_files


def _convert_to_int(byte_array, stride=2):
    """Converts a byte array to a list with specific
    integer values. Byte arrays is typically a sequence
    of hexadecimal values '\x00\x01\x00\x02' and with
    default values, this function splits this array to [1,2].

    Args:
        byte_array (bytearray): The byte array to be converted
        stride (int, optional): How many bytes per value, 2 for
        32bit and 4 for 64bit. Defaults to 2.

    Returns:
        list: a list with all the converted bytes.
    """
    int_array = [
        int.from_bytes(
            byte_array[byte:byte + stride],  # Slicing the size of an int
            byteorder="little",
            signed=True
        )
        for byte in range(0, len(byte_array), stride)
    ]

    return int_array


def read_data(filename):
    """Opening and reading file in binary mode."""
    with open(filename, "rb") as file:
        data = file.read()

    int_array = _convert_to_int(data)

    return int_array


# funktion för att gå och läsa ur datan ur
# funktion för göra om till rätt byte-format 32 eller 64 bitars
