import os
import sys
import click
import parser

folder_help = "Folder where the data is stored. If not specified " \
              "defaults to current working directory. The folder " \
              "given will be searched for data files down to " \
              "three levels of sub directories."
output_help = "Output file to write to. If not specified defaults " \
              "to output.csv"
list_help = "List all the data files found in the specific folder."
big_amount_of_data = "This is a big amount of data files and might " \
                     "take some time to compute, are you sure you " \
                     "want to continue? (y/n)\n"


@click.command()
@click.option('--folder', '-f', default=os.getcwd(), help=folder_help)
@click.option('--output', '-o', default="output.csv", help=output_help)
@click.option('--list', '-l', is_flag=True, help=list_help)
def cli(folder, output, list):
    file_list = parser.list_data_files(folder)

    if len(file_list) > 8:
        answer = input(big_amount_of_data)
        if not ((answer == 'y') or (answer == 'Y')):
            sys.exit(0)

    data = parser.read_data("/mnt/c/software/python/acp_parser/acp_parser/data/W1505 800 Broken blade 800rpm Test 6/testdir/dacval[0]")
    print(data[0:50])
    # If [-l, --list] is specified, list all the data files.

    if list:
        lista = parser.list_data_files(folder)
        for item in lista:
            click.echo(item)


# For testing purposes during development only.
if __name__ == "__main__":
    cli()
