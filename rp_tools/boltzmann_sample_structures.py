from pathlib import Path
from argparse import ArgumentParser
from functions import boltzmann_sample_folder


def read_single_arguments():
    """
    Command line reader
    """
    description_string = "This script will create a file where the 0th entry is the structure that has the highest boltzmann probability from a folder of structure.xyz files"
    parser = ArgumentParser(description=description_string)
    parser.add_argument(
        "-f",
        "--folder_path",
        dest="f",
        type=str,
        required=True,
        help="path to folder containing all structure.xyz files",
    )


def main():
    args = read_single_arguments()

    fp = Path(args.f)

    boltzmann_sample_folder(fp)
    

if __name__ == "__main__":
    main()
