import parser

data_files = parser.list_data_files()

for file in data_files:
    print(f"{file}")
