import parser
import os
import sys

data_files = parser.list_data_files()

for file in data_files:
    print(f"{file}")