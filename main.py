import parser
import timer

data_files = timer.time_it(parser.list_data_files)

for file in data_files:
    print(f"{file}")
