import parser
import timer

data_files = timer.time_it(parser.list_data_files)


def main():
    for file in data_files:
        print(f"{file}")

if __name__ == "__man__":
    main()
