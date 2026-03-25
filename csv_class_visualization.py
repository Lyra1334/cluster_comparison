import argparse

from absl import app
from absl.flags import argparse_flags
from shutil import copytree
from os import mkdir
from os.path import join

def parse_args(argv):
    parser = argparse_flags.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--csv_file",
        type=str,
        help="Input file to be read.",
        default="/home/mari/pibic/comp_centroides/filtrado.csv"
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        help="File to write output.",
        default="/home/mari/pibic/comp_centroides/clusters"
    )
    parser.add_argument(
        "--data_folder",
        type=str,
        help="Folder to look for the original folders in.",
        default="/home/mari/pibic/tudo"
    )
    parser.add_argument(
        "--lines",
        type=int,
        help="Number of lines to be read and copied from the csv.",
        default=50
    )
    args = parser.parse_args(argv[1:])
    return args

def main(args):
    
    with open(args.csv_file, "r") as csv:
        for line in range(args.lines):
            mkdir(join(args.ouput_folder,str(line+1)))
            text = csv.readline().strip()
            if text == "":
                print(f"Csv acabou após {line+1} linhas.")
                return
            paths = csv.readline().strip().split(",")
            copytree(join(args.data_folder,paths[0]),join(args.output_folder,str(line+1)))
            copytree(join(args.data_folder,paths[1]),join(args.output_folder,str(line+1)))
    print(f"Processo acabou após {args.lines} linhas.")
    return


if __name__ == "__main__":
    app.run(main,flags_parser=parse_args)