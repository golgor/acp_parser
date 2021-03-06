import sys
import click
from parser import Parser

folder_help = (
    "Folder where the data is stored. If not specified "
    "defaults to current working directory. The folder "
    "given will be searched for data files down to "
    "three levels of sub directories."
)
output_help = (
    "Output file to write to. If not specified defaults "
    "to output.csv"
)
batch_help = "Batch processing of all data in the given folder."
big_amount_of_data = (
    "This is a big amount of data files and might "
    "take some time to compute, are you sure you "
    "want to continue? (y/n)\n"
)


@click.command()
@click.option("--folder", "-f", default=None, help=folder_help)
@click.option("--output", "-o", default="output.csv", help=output_help)
@click.option("--batch", "-b", is_flag=True, help=batch_help)
def cli(folder, output, batch):
    parser = Parser(folder)

    data_folder = parser.get_data_folders()

    if batch:
        print("Batch processing following data:")
        for idx, folder in enumerate(data_folder, 1):
            print(f"{idx}. {folder.get_title()}")
        sys.exit(0)

    # If more than one data folder is found gives the user
    # options to which data should be processed.
    if len(data_folder) > 1:
        print("Following data folders found:\n")
        for idx, folder in enumerate(data_folder, 1):
            print(f"{idx}. {folder.get_title()}")

        print(
            "\nChoose what data to process, one or multiple choices "
            'possible. Choice separated with <space> i.e. "1 3"'
        )

        choices_s = (
            input("What data do you want to process?" " Default: 1.\n").split()
        ) or [1]

        choices = list(map(int, choices_s))

        if not len(choices) == len(set(choices)):
            print("\nDuplicate values found. "
                  "Please only enter each option once!")

        if max(choices) > len(data_folder):
            print("Wrong input. You can choose between 1 and "
                  f"{len(data_folder)}.")
            sys.exit(1)

        print("Processing files!")

    # If only one folder is found, ask if the user wants
    # to start processing the found folder.
    elif len(data_folder) == 1:
        print(f"{data_folder[0].get_title()} was found")
        if input("Do you want to process the files?"):
            print("Processing files!")
    # If no files found, just exit.
    else:
        print("No data folder found!")


# For testing purposes during development only.
if __name__ == "__main__":
    cli()
